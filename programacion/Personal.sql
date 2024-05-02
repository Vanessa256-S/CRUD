CREATE DATABASE Personal
USE Personal
CREATE TABLE PersonalActivo (
    PersonaID INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100),
    Apellido NVARCHAR(100),
	FechaNacimiento DATE,
	Telefono NVARCHAR(20),
    Email NVARCHAR(100),
	Cargo NVARCHAR (100),
	Salario bigint,
);

insert into PersonalActivo (Nombre, Apellido, FechaNacimiento,Telefono, Email, Cargo,Salario)
	values (
		'Fernando', 'Perez', '2001-10-01','3113113110', 'fp@gmail.com', 'Administrador','1000000');

select * from PersonalActivo
