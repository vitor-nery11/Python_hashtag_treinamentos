from datetime import datetime, timedelta

hoje = datetime.now()

amanha = hoje + timedelta(days=1)

print(amanha)

# mais exemplos 

nova_data1= hoje + timedelta(days= 7)
nova_data2 = hoje + timedelta(days= 2)
nova_data3 = hoje + timedelta(days= 30)

print(nova_data1)
print(nova_data2)
print(nova_data3)

