from datetime import datetime, timedelta

hoje = datetime.now()

amanha = hoje + timedelta(days=1)

print(amanha)