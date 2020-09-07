--���ݿ�ϵͳ����

/*
 T-SQL��Transact-SQL������Mcrosoft SQL Sever�ϵ���ǿ��
    SQL severר�ñ�׼�ṹ����ѯ������ǿ��

 set һ��ֻ�ܸ�ֵһ������
 select ����һ�θ�ֵ�������
 */

declare @myvar char(20);
set @myvar='Hello world!'
print @myvar

declare @var1 date,@var2 char(10)
set @var1=getdate()
set @var2 = convert(char(10),@var1,102)
print '�����������'+@var2

print @@version
print @@servername
print @@servicename

/*
ѡ��ṹ
ѭ���ṹ
*/

--������û��ѧ��Ϊ201215120��ѧ�����еĻ���ʾѧ����Ϣ
--û����ʾû�ҵ�

if exists(select * from student where sno='201215120')
begin
	select * from student where sno='201215120'
end
else
	print 'û���ҵ���'

/*
��ѧ����Student�У�ѡȡSno ,SSEX , ���SSEXΪ���������M����
���Ϊ��Ů�����������F��
*/

select sno,ssex=
		case ssex
		when '��' then  'M'
		when 'Ů' then 'F'
		end
from student

--ѭ���ṹ

/*�� 1 ~ 10�ĺ�*/
declare @X int ,@sum int
set @X=0
set @sum=0
while @X<10
	begin
		set @X=@X+1 
		set @sum=@sum+@X
		print 'sum = '+convert(char(2),@sum)
	end


--�ȴ����
/*1�����õȴ�һСʱ��ִ�в�ѯ*/
begin 
	waitfor delay '1:00:00'
	select * from student
end

/*2�����õ�ʮ����ִ�в�ѯ*/
begin
	waitfor time '10:00:00'
	select * from sc
end

/*ʹ�����ں��������Լ����ڵ�����*/
select '����'=
	datediff(YY,'1979-06-01',getdate())

/*����ָ����������/��/�յ�����*/
select year('2016-01-08')

/*��ȡѧ���е���ѧ���*/
print substring('2018011702',1,4)

--�α�
/*
�α���һ���ܴӰ����������ݼ�¼�Ľṹ����ÿ����ȡһ����¼�Ļ���
�α��ʹ��
    �����α�
    ���α�
    ��ȡ�α��е�����
    �ر��α�
    �ͷ��α�

@@fetch_status������������ͬ�ķ���ֵ
    0 �� fetch���ִ�гɹ�
    -1��fetch���ִ��ʧ�ܻ������ݳ����α����ݽ�����ķ�Χ
    -2����ʾ��ȡ�����ݲ�����
*/

/*����һ���α꣬ͳ��û��ѡ�޿γ̵�ѧ������*/

declare @sno char(9),@num int
set @num=0
--�����α�
declare num_cursor cursor
for 
	select sno
	from student
	for read only
--���α�
open num_cursor
--���α��ж�ȡ����
fetch next from num_cursor into @sno
while @@fetch_status=0
	begin
		if not exists(select * from sc where sno=@sno)
			set @num=@num+1
		fetch next from num_cursor into @sno
	end
print 'û��ѡ�ε�������'+convert(char(2),@num)


--�ر��α�
close num_cursor
--�ͷ��α�
deallocate num_cursor



/*
    �洢����
    �洢���̣�Stored Procedure����һ������ض����ܵ�SQL��伯
    ���������洢�����ݿ��У��û�ͨ���ƶ��洢���̵����ֲ���������
    ������ô洢���̴��в�������ִ�д洢����

    �洢���̵��ŵ�
        �洢�������ڷ�����ע��
        �洢���̾��а�ȫ����
        �洢���̿���ǿ��Ӧ�ó���İ�ȫ��
        �洢��������ģ�黯�������
        �洢���̿��Լ�������ͨ������

    �����洢����  create
    ִ�д洢����  execute
    ɾ���洢����  drop

 */

--�洢����
--1)��ѯ�������Ŵγ���1�ŵ�ѧ���Ļ�����Ϣ

--�����洢����
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

--2) ������ѧ����¼��װ��һ���洢����
create proc proc_insert_student
@sno char(9),
@sname char(10),
@ssex char(2)='��',
@sage int,
@sdept varchar(20)
as
begin
    insert into Student(sno, sname, ssex, sage, sdept)
    values (@sno,@sname,@ssex,@sage,@sdept)
end


exec proc_insert_student '201215126','�¶�','��',18,'IS';

exec proc_insert_student @sno='201215127',@sname='�ų���',@sage=18,@sdept='IS';

--3)��ָ��ѧ�ŵ�ѧ����ƽ���ɼ�
create proc savggrade
@sno char(9),
--����͵���ʽ����
@savg smallint out
as
begin
    select avg(grade)
    from sc
    where sno = @sno
end

declare @avg_grade int  --�����ʵ�ʲ���
exec savggrade '201215121',@avg_grade out
select @avg_grade;

--4)��дһ���洢����proc_sum,�������ΪѧԺ���������Ϊ����������Ϊ����
--�����ѧԺ��������ѧ������
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
 SQL sever 2008 ֧��3�����͵�Transact-SQL�û��Զ��庯����
    ��������
    ��Ƕ��ֵ����
    ������ֵ����

 �ŵ㣺
    ����ģ�黯�������
    ִ���ٶȸ���
    ������������
 */

 --�Զ��庯��������һ������ʱ�������
create function dateonly (@date datetime)
returns varchar(12)
as
begin
    return convert(varchar(12),@date,101)
end

select dbo.dateonly(getdate());

--����һ��������ͳ�Ʋ�ͬ�����������˵������
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

--��Ƕ��ֵ����������һ�ű�

-- ����һ������������ѧ��������
create function fun1()
returns table
as
    return select sno,sname from Student

select *
from fun1()

--����һ����������ָ��ϵ��ѧ����ƽ���ɼ�
create function avg_grade(@sdept varchar(10))
returns table
as
    return select sc.sno,avg(grade) '�ɼ�'
    from Student left join sc on Student.sno=sc.sno
    where Student.Sdept=@sdept
    group by sc.sno

select *
from avg_grade('CS')


--������

-- ����һ��������������SC����������ǣ����student�����Ƿ���ڣ���������ɾ��
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


--����һ����������Ҫ����ӻ��޸ĳɼ�������0~100֮��
create trigger tr_sc_grade
on sc
after insert,update
as
begin
    declare @grade int
    select @grade=grade from inserted
    if(@grade<0 or @grade>100)
        begin
            --��ʾ
            raiserror('�ɼ�������0��100֮��',16,10)
            -- ����Կ�ף�֮ǰ���в���������
            rollback transaction
        end
end

--���ݿ�ϵͳ����

/*
 T-SQL��Transact-SQL������Mcrosoft SQL Sever�ϵ���ǿ��
    SQL severר�ñ�׼�ṹ����ѯ������ǿ��

 set һ��ֻ�ܸ�ֵһ������
 select ����һ�θ�ֵ�������
 */

declare @myvar char(10);
set @myvar='Hello world!'
print @myvar







