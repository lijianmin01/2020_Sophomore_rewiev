--创建数据库

create database Student1;

use Student1;

CREATE TABLE Student
(
    Sno   char(9) primary key,
    Sname Varchar(20) unique,
    Ssex  char(2),
    Sage  smallint,
    Sdept char(20)
);

create table course(
    Cno char(4) primary key,
    cname char(40),
    cpno char(4), /*先修课*/
    ccredit smallint,
    foreign key(cpno) references course(cno)
);

create table sc(
    sno char(9),
    cno char(4),
    grade smallint,
    primary key (sno,cno),
    foreign key(sno) references student(sno),
    foreign key(cno) references course(cno)

);


/* 常用的完整性约束
主码约束： primary key
非空值约束： not null
参照完整性约束： foreign key
*/

--插入数据
insert student values ('201215121','李勇','男',20,'CS');
insert student values ('201215122','刘晨','女',19,'CS');
insert student values ('201215123','王敏','女',18,'MA');
insert student values ('201215125','张立','男',19,'IS');

insert course values('1','数据库','5',4);
insert course values('2','数学',null,2);
insert course values('3','信息系统','1',4);
insert course values('4','操作系统','6',3);
insert course values('5','数据结构','7',4);

insert course values('6','数据处理',null,2);
insert course values('7','PASCAL语言','6',4);

insert sc values('201215121','1',92);
insert sc values('201215121','2',85);
insert sc values('201215121','3',88);
insert sc values('201215122','2',90);
insert sc values('201215122','1',80);

/*  创建索引

 */

-- 建立索引
-- create index stusno on Student(sno asc);
-- create cascaded

-- 查询年龄在10~20岁之间的所有学生   18\ 19 都要
select sname,Sdept,Sage
from Student
where sage between 18 and 19;