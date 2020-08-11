/*
 创建SqlReview数据库
 */
create database SqlReview;
/*
 * 使用SqlReview
 */
use SqlReview;

--建立学生表Student
create table Student(
	Sno char(6) primary key,
	Sname char(4) unique,
	Ssex char(2),
	Sage smallint,
	Sdept char(4)
);

--DROP table SC;
--DROP table Course;
--建立课程关系Course
create table Course(
	Cno char(6) primary key,
	Cname varchar(9) unique,
	Cpno char(2),
	Ccredit smallint,
	foreign key(Cno) references Course(Cno)
);
--建立sc
create table SC(
	Sno char(6),
	Cno char(6),
	Grade smallint,
	primary key(Sno,Cno),
	foreign key(Sno) references Student(Sno),
	foreign key(Cno) references Course(Cno)
);

--插入数据
insert Student into values('201215121','李勇','男',20,'CS');
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


/*
 * 修改基本表：
 * 		add : 增加新列和新的完整性约束条件
 * 		drop : 删除指定的完整性约束条件
 * 		alter column: 用于修改列名和数据类型	
 */


--将年龄的数据类型由字符型（假设原来的数据类型是字符型）改为整数
alter table Student alter column Sage int;

--增加课程名必须取唯一值
alter table Course add unique(Cname); 


/*删除基本表:
 *	drop table <表名> [restrict | cascade]
 * 	restrict :删除表有限制的（如果存在依赖该表的表，则此表不能被删除）
 * 	cascade: 强制删除（并且与该表有关系的表会一并删除。视图也会被删除）
 */

/*	索引：
 * 		为学生-课程数据库中的Student，Course，SC三个表
 * 建立索引。其中Student表按学号升序建唯一索引，
 * Course表按课程号升序建唯一索引，
 * SC表按学号升序和课程号降序建唯一索引。
 * 
 */

create unique index stusno1 on student(sno);
create unique index coucon1 on course(cno);
-- asc 升序		desc 降序
create unique index scno1 on sc(sno asc,cno desc);










