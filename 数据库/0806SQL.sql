/*
 ����SqlReview���ݿ�
 */
create database SqlReview;
/*
 * ʹ��SqlReview
 */
use SqlReview;

--����ѧ����Student
create table Student(
	Sno char(6) primary key,
	Sname char(4) unique,
	Ssex char(2),
	Sage smallint,
	Sdept char(4)
);

--DROP table SC;
--DROP table Course;
--�����γ̹�ϵCourse
create table Course(
	Cno char(6) primary key,
	Cname varchar(9) unique,
	Cpno char(2),
	Ccredit smallint,
	foreign key(Cno) references Course(Cno)
);
--����sc
create table SC(
	Sno char(6),
	Cno char(6),
	Grade smallint,
	primary key(Sno,Cno),
	foreign key(Sno) references Student(Sno),
	foreign key(Cno) references Course(Cno)
);

--��������
insert Student into values('201215121','����','��',20,'CS');
insert student values ('201215122','����','Ů',19,'CS');
insert student values ('201215123','����','Ů',18,'MA');
insert student values ('201215125','����','��',19,'IS');

insert course values('1','���ݿ�','5',4);
insert course values('2','��ѧ',null,2);
insert course values('3','��Ϣϵͳ','1',4);
insert course values('4','����ϵͳ','6',3);
insert course values('5','���ݽṹ','7',4);
insert course values('6','���ݴ���',null,2);
insert course values('7','PASCAL����','6',4);

insert sc values('201215121','1',92);
insert sc values('201215121','2',85);
insert sc values('201215121','3',88);
insert sc values('201215122','2',90);
insert sc values('201215122','1',80);


/*
 * �޸Ļ�����
 * 		add : �������к��µ�������Լ������
 * 		drop : ɾ��ָ����������Լ������
 * 		alter column: �����޸���������������	
 */


--������������������ַ��ͣ�����ԭ���������������ַ��ͣ���Ϊ����
alter table Student alter column Sage int;

--���ӿγ�������ȡΨһֵ
alter table Course add unique(Cname); 


/*ɾ��������:
 *	drop table <����> [restrict | cascade]
 * 	restrict :ɾ���������Ƶģ�������������ñ�ı���˱��ܱ�ɾ����
 * 	cascade: ǿ��ɾ����������ñ��й�ϵ�ı��һ��ɾ������ͼҲ�ᱻɾ����
 */

/*	������
 * 		Ϊѧ��-�γ����ݿ��е�Student��Course��SC������
 * ��������������Student��ѧ������Ψһ������
 * Course���γ̺�����Ψһ������
 * SC��ѧ������Ϳγ̺Ž���Ψһ������
 * 
 */

create unique index stusno1 on student(sno);
create unique index coucon1 on course(cno);
-- asc ����		desc ����
create unique index scno1 on sc(sno asc,cno desc);










