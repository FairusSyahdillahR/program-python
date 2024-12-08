print ("##--------PROGRAM KONVERSI REAMUR--------##" );
print("=============================================");
print("=============================================");
print();
print();

reamur = float(input('Masukkan suhu Reamur :'));
print('Suhu adalah',reamur,'Reamur');

#Celcius 
celcius = (5/4)*reamur;
print(reamur,'derajat Reamur =',celcius,'derajat Celcius')

#Fahrenheit
fahrenheit = ((9/4)*reamur)+32;
print(reamur,'derajat Reamur =',fahrenheit,'derajat Fahrenheit')

#Kelvin
kelvin = ((5/4)*reamur)+273;
print(reamur,'derajat Reamur =',kelvin,'derajat Kelvin')