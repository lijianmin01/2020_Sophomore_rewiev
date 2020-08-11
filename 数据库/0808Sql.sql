create database jd_questions;

use jd_questions;

-- 学生表 Student
create table Student(
    SId varchar(10),
    Sname varchar(10),
    Sage datetime,
    Ssex varchar(10));

insert into Student values('01' , '赵雷' , '1990-01-01' , '男');
insert into Student values('02' , '钱电' , '1990-12-21' , '男');
insert into Student values('03' , '孙风' , '1990-12-20' , '男');
insert into Student values('04' , '李云' , '1990-12-06' , '男');
insert into Student values('05' , '周梅' , '1991-12-01' , '女');
insert into Student values('06' , '吴兰' , '1992-01-01' , '女');
insert into Student values('07' , '郑竹' , '1989-01-01' , '女');
insert into Student values('09' , '张三' , '2017-12-20' , '女');
insert into Student values('10' , '李四' , '2017-12-25' , '女');
insert into Student values('11' , '李四' , '2012-06-06' , '女');
insert into Student values('12' , '赵六' , '2013-06-13' , '女');
insert into Student values('13' , '孙七' , '2014-06-01' , '女');


--科目表 Course
create table Course(
    CId varchar(10),
    Cname nvarchar(10),
    TId varchar(10));
insert into Course values('01' , '语文' , '02');
insert into Course values('02' , '数学' , '01');
insert into Course values('03' , '英语' , '03');

--教师表 Teacher
create table Teacher(
    TId varchar(10),
    Tname varchar(10));
insert into Teacher values('01' , '张三');
insert into Teacher values('02' , '李四');
insert into Teacher values('03' , '王五');

--成绩表 Sc
create table SC(
    SId varchar(10),
    CId varchar(10),
    score decimal(18,1));
insert into SC values('01' , '01' , 80);
insert into SC values('01' , '02' , 90);
insert into SC values('01' , '03' , 99);
insert into SC values('02' , '01' , 70);
insert into SC values('02' , '02' , 60);
insert into SC values('02' , '03' , 80);
insert into SC values('03' , '01' , 80);
insert into SC values('03' , '02' , 80);
insert into SC values('03' , '03' , 80);
insert into SC values('04' , '01' , 50);
insert into SC values('04' , '02' , 30);
insert into SC values('04' , '03' , 20);
insert into SC values('05' , '01' , 76);
insert into SC values('05' , '02' , 87);
insert into SC values('06' , '01' , 31);
insert into SC values('06' , '03' , 34);
insert into SC values('07' , '02' , 89);
insert into SC values('07' , '03' , 98);

-- 1.查询" 01 "课程比" 02 "课程成绩高的学生的信息及课程分数
select SSC.SId, SSC.Sname, SSC.Sage, SSC.Ssex, sc1.score '01分数',sc2.score '02分数' from (Student SSC left join SC sc1 on SSC.SId = sc1.SId)
    left join SC sc2 on sc2.SId=SSC.SId
where sc1.CId='01'and SSC.SId=sc2.SId and sc2.CId='02' and sc1.score>sc2.score and SSC.SId in (
    select SId
    from SC
    where CId = '01'
      and SId in (
        select SId
        from SC
        where CId = '02'
    )
)

/*嵌套查询*/
select * from(
             select t1.sid,score1,score2 from
                                              (select sid,score as score1 from sc where sc.cid='01') as t1,
                                              (select sid,score as score2 from sc where sc.cid = '02') as t2
             where t1.sid = t2.sid and t1.score1 > t2.score2) as r
                 left join student on student.sid = r.sid
-- 2.查询同时存在" 01 "课程和" 02 "课程的学生数据

/*
 并操作 union
 交操作 intersect
 差操作 except

 */
select * from Student where  SId in (
    select SId
    from SC
    where CId = '01'
      and SId in (
        select SId
        from SC
        where CId = '02'
    )
)

select * from Student where SId in(
    select SId from SC where CId='01'
    intersect
    select SId from SC where CId='02'
);
-- 3.查询存在" 01 "课程但可能不存在" 02 "课程的情况(不存在时显示为 null )
select * from Student where  SId in (
    select SId
    from SC
    where CId = '01'
      and SId not in (
        select SId
        from SC
        where CId = '02'
    )
)

select * from Student where SId in(
    select SId from SC where CId='01'
    except
    select SId from SC where CId='02'
);
-- 4.查询不存在" 01 "课程但存在" 02 "课程的情况
select * from Student where  SId in (
    select SId
    from SC
    where CId = '02'
      and SId not in (
        select SId
        from SC
        where CId = '01'
    )
)

select * from Student where SId in(
    select SId from SC where CId='02'
        except
    select SId from SC where CId='01'
);

-- 5.查询平均成绩大于等于 60 分的同学的学生编号和学生姓名和平均成绩
select Student.SId,Sname,avg(score) from Student left join SC on Student.SId=SC.SId group by Student.SId, Sname having avg(score)>=60;

select st.sid,st.sname,r.avg_score
from student as st,(select sid,avg(score) as avg_score from sc group by sid having avg(score) >60) as r
where st.sid = r.sid;

-- 6.查询所有同学的学生编号、学生姓名、选课总数、所有课程的成绩总和
select distinct st.SId,st.Sname,csc '选课总数',ssc '成绩总和'from Student as st ,(select distinct Student.SId,count(score) as csc,sum(score) as ssc from Student left join sc on Student.SId=sc.SId group by Student.SId ) as r
where st.SId=r.SId;

select Student.SId,Sname,course_num '选课总数',sum_score '成绩总和'from Student left join (select distinct sid,count(score) as course_num,sum(score) as sum_score from sc group by SId) as r on Student.SId=r.SId;

select s.sid,s.sname,t.cnums,t.scoresum
from ((select st.sid,st.sname from student as st) as s
         left join
     (select sc.sid,count(sc.cid) as cnums,sum(sc.score) as scoresum
      from sc
      group by sc.sid)as t
     on s.sid = t.sid)

-- 7.查询学过「张三」老师授课的同学的信息
select * from Student where sid in (
        select sid from sc where CId in (
            select CId from Course where TId in(
                select TId from Teacher where Tname='张三'
                )
            )
    )

select st.*
from student as st,course,teacher,sc
where st.sid = sc.sid
  and sc.cid = course.cid
  and course.tid = teacher.tid
  and teacher.tname = '张三'

-- 8. 查询没有学全所有课程的同学的信息
select * from Student where SId in(
    select SId from SC group by SId having count(CId) !=3
    )

-- 9.查询至少有一门课与学号为" 01 "的同学所学相同的同学的信息
select * from Student where SId in(
    select SId from SC where CId in (
        select CId from sc where SId='01'
    )
)
-- 10.查询和" 01 "号的同学学习的课程完全相同的其他同学的信息
/*
先确定与01同学课程数目一致的同学，在确定同学所学的科目都在01中
 */
 select distinct Student.SId, Sname, Sage, Ssex from Student ,sc where sc.SId in (
     select SId from SC group by SId having SId!='01' and count(score)=(
         select count(score) from SC group by SId having SId='01'
         )
 ) and sc.SId=Student.SId and sc.CId in(
     select CId from SC as S1 where S1.SId='01'
     )

-- 11. 查询没学过"张三"老师讲授的任一门课程的学生姓名
select * from Student where SId not in (
    select distinct SId from sc where CId in (
        select CId from Course where TId in (
            select Teacher.TId from Teacher where Tname='张三'
        )
    )
)

select *
from student as st
where st.sid not in (
    select sid	from sc where sc.cid in (
        select course.cid from course where course.tid  in (
            select tid from teacher where tname = '张三')));

select * from student
where student.sid not in (select sc.sid from course,sc,teacher
                          where sc.cid = course.cid
                            and course.tid = teacher.tid
                            and tname = '张三');
-- 12.查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
select st.sid,st.sname,avg(sc.score) as avg_score
from Student as st,SC
where st.SId=sc.SId
and sc.score<60
group by st.sid, st.sname having count(*)>=2;


-- 13.检索" 01 "课程分数小于 60，按分数降序排列的学生信息
select *
from Student ,SC where Student.sid=SC.SId and sc.CId='01' order by score desc;

-- 14. 按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩
select sid,cid,score from sc
union
select  r.sid,'avg',r.avg_1 from(select sid,avg(score) as avg_1 from sc group by SId) as r


select SId,avg(score) from sc group by SId
-- 15.查询各科成绩最高分、最低分和平均分，选修人数，及格率，中等率，优良率，优秀率：
--
-- 16.按各科成绩进行排序，并显示排名， Score 重复时保留名次空缺
--
-- 17.查询学生的总成绩，并进行排名，总分重复时不保留名次空缺
--
-- 18.统计各科成绩各分数段人数：课程编号，课程名称，[100-85]，[85-70]，[70-60]，[60-0] 及所占百分比
--
-- 19.查询各科成绩前三名的记录
--
-- 20.查询出只选修两门课程的学生学号和姓名
--
-- 21. 查询同名学生名单，并统计同名人数
--
-- 22. 查询 1990 年出生的学生名单
--
-- 23.查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
--
-- 24.查询平均成绩大于等于 85 的所有学生的学号、姓名和平均成绩
--
-- 25.查询课程名称为「数学」，且分数低于 60 的学生姓名和分数
--
-- 26.查询所有学生的课程及分数情况（存在学生没成绩，没选课的情况）
--
-- 27.查询任何一门课程成绩在 70 分以上的姓名、课程名称和分数
--
-- 28. 查询存在不及格的课程
--
-- 29.查询课程编号为 01 且课程成绩在 80 分及以上的学生的学号和姓名
--
-- 30.成绩有重复的情况下，查询选修「张三」老师所授课程的学生中，成绩最高的学生信息及其成绩
--
-- 31.查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩
--
-- 32.查询每门功成绩最好的前两名
--
-- 33. 统计每门课程的学生选修人数（超过 5 人的课程才统计
--
-- 34.检索至少选修两门课程的学生学号
--
-- 35.查询选修了全部课程的学生信息
--
-- 36. 按照出生日期来算，当前月日 < 出生年月的月日则，年龄减一
--
-- 37.查询本周过生日的学生
--
-- 38.查询下周过生日的学生
--
-- 39.查询本月过生日的学生
--
-- 40. 查询下月过生日的学生