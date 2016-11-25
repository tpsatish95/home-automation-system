use has;

drop table room1;
drop table room2;

create table room1 (devNum varchar(20), status int);
create table room2 (devNum varchar(20), status int);

insert into room1 values("Dev1",0);
insert into room1 values("Dev2",0);
insert into room1 values("Dev3",0);
insert into room1 values("Dev4",0);

select * from room1;

insert into room2 values("Dev1",0);
insert into room2 values("Dev2",0);
insert into room2 values("Dev3",0);
insert into room2 values("Dev4",0);

select * from room2;
