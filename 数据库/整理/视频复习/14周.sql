
/*
    存储过程
    存储过程（Stored Procedure）是一组完成特定功能的SQL语句集
    ，经编译后存储在数据库中，用户通过制定存储过程的名字并给出参数
    （如果该存储过程带有参数）来执行存储过程

    存储过程的优点
        存储过程已在服务器注册
        存储过程具有安全特性
        存储过程可以强制应用程序的安全性
        存储过程允许模块化陈旭设计
        存储过程可以减少网络通信流量

    创建存储过程  create
    执行存储过程  execute
    删除存储过程  drop

 */

--存储过程
--1)查询不及格门次超过1门的学生的基本信息

--创建存储过程
create proc  myproc
as
begin
select *
from student
where sno in (
        select sno
        from sc
        where grade<60
        group by sno
        having count(*)>=1
    )
end

exec myproc;

--2) 将插入学生记录封装成一个存储过程
create proc proc_insert_student
@sno char(9),
@sname char(10),
@ssex char(2)='男',
@sage int,
@sdept varchar(20)
as
begin
    insert into Student(sno, sname, ssex, sage, sdept)
    values (@sno,@sname,@ssex,@sage,@sdept)
end


exec proc_insert_student '201215126','陈东','男',18,'IS';

exec proc_insert_student @sno='201215127',@sname='张成民',@sage=18,@sdept='IS';

--3)求指定学号的学生的平均成绩
create proc savggrade
@sno char(9),
--输出型的形式参数
@savg smallint out
as
begin
    select avg(grade)
    from sc
    where sno = @sno
end

declare @avg_grade int  --输出型实际参数
exec savggrade '201215121',@avg_grade out
select @avg_grade;

--4)编写一个存储过程proc_sum,输入参数为学院，输出参数为人数，功能为根据
--输入的学院，并返回学生人数
create proc proc_sum
@sdept_cnt char(10),
@student_sum int out
as
begin
    select count(*)
    from Student
    where Sdept=@sdept_cnt
end

declare @stu_sum int
exec proc_sum 'IS',@stu_sum out
select @stu_sum;

/*
 SQL sever 2008 支持3种类型的Transact-SQL用户自定义函数：
    标量函数
    内嵌表值函数
    多语句表值函数

 优点：
    允许模块化程序设计
    执行速度更快
    减少网络流量
 */

 --自定义函数，返回一个不带时间的日期
create function dateonly (@date datetime)
returns varchar(12)
as
begin
    return convert(varchar(12),@date,101)
end

select dbo.dateonly(getdate());

--定义一个函数，统计不同出生年靓的人的年龄段
create function whichgeneration(@birthday datetime)
returns varchar(12)
as
begin
    if year(@birthday) < 1980
        return 'Too Old !'
    else if year(@birthday) < 1990
        return '80s'
    else
        return '90s'
    return 0
end


select dbo.whichgeneration('1999-12-20')
select dbo.whichgeneration('1979.12.20')

--内嵌表值函数，返回一张表

-- 创建一个函数。返回学生的姓名
create function fun1()
returns table
as
    return select sno,sname from Student

select *
from fun1()

--创建一个函数，求指定系的学生的平均成绩
create function avg_grade(@sdept varchar(10))
returns table
as
    return select sc.sno,avg(grade) '成绩'
    from Student left join sc on Student.sno=sc.sno
    where Student.Sdept=@sdept
    group by sc.sno

select *
from avg_grade('CS')


--触发器

-- 创建一个触发器，当往SC表添加数据是，检查student表中是否存在，不存在则删除
create trigger tr_insert_sc
on sc
after insert
as
begin
    declare @sno char(9)
    select @sno=sno from inserted
    if not exists(select * from student where sno=@sno)
        delete from sc where sno=@sno
end


--创建一个触发器，要求添加会修改成绩必须在0~100之间
create trigger tr_sc_grade
on sc
after insert,update
as
begin
    declare @grade int
    select @grade=grade from inserted
    if(@grade<0 or @grade>100)
        begin
            --提示
            raiserror('成绩必须在0到100之间',16,10)
            -- 万能钥匙，之前所有操作不算数
            rollback transaction
        end
end

--数据库系统概论

/*
 T-SQL即Transact-SQL，是在Mcrosoft SQL Sever上的增强版
    SQL sever专用标准结构化查询语言增强版

 set 一次只能赋值一个变量
 select 可以一次赋值多个变量
 */

declare @myvar char(10);
set @myvar='Hello world!'
print @myvar
















