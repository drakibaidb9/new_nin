 

import base64, codecs
magic = 'aW1wb3J0IHJhbmRvbQppbXBvcnQgc3lzCmltcG9ydCB3ZWJzb2NrZXQKaW1wb3J0IHRocmVhZGluZwppbXBvcnQgdGltZQppbXBvcnQganNvbgppbXBvcnQgbG9nZ2luZwppbXBvcnQgc29ja2V0CmltcG9ydCBzc2wKaW1wb3J0IHJlbApmcm9tIGxvZ2dpbmcuaGFuZGxlcnMgaW1wb3J0IFN5c0xvZ0hhbmRsZXIKY2xhc3MgQ29udGV4dEZpbHRlcihsb2dnaW5nLkZpbHRlcik6CiAgICBob3N0bmFtZSA9IHNvY2tldC5nZXRob3N0bmFtZSgpCiAgICBkZWYgZmlsdGVyKHNlbGYsIHJlY29yZCk6CiAgICAgICAgcmVjb3JkLmhvc3RuYW1lID0gIm9wdXMtMiIKICAgICAgICByZXR1cm4gVHJ1ZQpzeXNsb2cgPSBTeXNMb2dIYW5kbGVyKGFkZHJlc3M9KCdsb2dzMi5wYXBlcnRyYWlsYXBwLmNvbScsIDQ3MDA4KQpzeXNsb2cuYWRkRmlsdGVyKENvbnRleHRGaWx0ZXIoKSkKZm9ybWF0ID0gJyUoYXNjdGltZSlzICUoaG9zdG5hbWUpcyBFYXJuaWZ5IEJvdDogJShtZXNzYWdlKXMnCmZvcm1hdHRlciA9IGxvZ2dpbmcuRm9ybWF0dGVyKGZvcm1hdCwgZGF0ZWZtdD0nJWIgJWQgJUg6JU06JVMnKQpzeXNsb2cuc2V0Rm9ybWF0dGVyKGZvcm1hdHRlcikKbG9nZ2VyID0gbG9nZ2luZy5nZXRMb2dnZXIoKQpsb2dnZXIuYWRkSGFuZGxlcihzeXNsb2cpCmxvZ2dlci5zZXRMZXZlbChsb2dnaW5nLklORk8pCnVzZXJuYW1lID0gJ2twc2luZ2gnCnBhc3N3b3JkID0gJ2Z1cWJZMS1ub25tZWctaGV2eGVmJwoiIiIKdXNlcm5hbWUgPSAiYmNsb3V0aWVyNDEyIgpwYXNzd29yZCA9ICJhaXNobGlubiIKCnVzZXJuYW1lID0gIm5heG1rcXJ5LXJvdGF0ZSIKcGFzc3dvcmQgPSAiY242cm83ZGZqdDRpIgoiIiIKY2hhbm5lbHMgPSBbIjB4OTBCMTAxMDk4NDBGQ0VDOEE'
love = '4BGOPAmt2DGN5BQMPZmZjARIOBGD5ZvVfVwO4DGL5DwqOZmN5ZxSREwAOAGx4DHWRAQuSBGZ5EwSPARSOARVmDHEPBPWqPaOlo3u5plN9VSfXVwR4BP43AP4lZGNhZwR6AwRjZPVfPvV0AF4kAGHhAwthZGV5BwtkZmZvYNbvZGH0Ywx1YwZ2YwR5BGb2BQxmVvjXVwD1Ywx0YwD3YwL2BwtkZGNvYNbvZGD0YwR2BP4lZGphBQt6BQp4ZPWqPtbXPz1mMmZtCFO7VaE5pTHvBvWlLKEyVvjvqzSfqJHvBwRjZQNjZQNjZQNjZQNjZQNjZQNjZQNjZU0XnaAioz1mMmZtCFOdp29hYzE1oKOmXT1mMmZcPzAfLKAmVUqmK2IuqPtcBtbXVPNtVTEyMvOioy9gMKAmLJqyXUEbnKZfq3ZfVT1yp3AuM2HcBtbtVPNtVPNtVNbtVPNtVPNtVNbtVPNtVPNtVTkiM2qypv5cozMiXT1yp3AuM2HcPvNtVPNtVPNtpUWcoaDboJImp2SaMFxXVPNtVPNtVPO3pl5mMJ5xXTcmo25gp2pmXDbXVPNtVTEyMvOioy9ypaWipvu0nTymYUqmYPOypaWipvx6PvNtVPNtVPNtpUWcoaDbMKWlo3VcPvNtVPNtVPNtoT9aM2IlYzIlpz9lXTIlpz9lXDbXVPNtVTEyMvOioy9woT9mMFu0nTymYUqmYPOwoT9mMI9mqTS0qKAsL29xMFjtL2kip2IsoKAaXGbXVPNtVPNtVPOjpzyhqPtvVlZwVTAfo3AyMPNwVlZvXDbtVPNtVPNtVTkiM2qypv53LKWhnJ5aXTAfo3AyK21mMlxXVPNtVPNtVPNXPvNtVPOxMJLto25so3Oyovu0nTymYUqmXGbXVPNtVPNtVPO3pl5mMJ5xXTcmo25gp2pkXDbtVPNtVPNtVUqmYaAyozDbnaAioz1mMmVcPvNtVPNtVPNtq3Zhp2IhMPudp29hoKAaZlxXVPNtVPNtVPNXPvNtVPOxMJLtq3AsqTulMJSxXUEbnKZfLJExpvkwYUOlo3u5XGbXVPNtVPNtVPNXVPNtVPNtVPObo3A0ozSgMFN9VPWaLKEyYzEwYaAgLKW0pUWirUxhL29gVtbtVPNtVPNtVUOipaDtCFNvZwNjZQNvPv'
god = 'AgICAgICAgIiIiCiAgICAgICAgaG9zdG5hbWUgPSAicC53ZWJzaGFyZS5pbyIKICAgICAgICBwb3J0ID0gIjgwIgogICAgICAgICIiIgogICAgICAgIG1zZzEgPSB7InR5cGUiOiJjaGFubmVsIiwidmFsdWUiOmN9CiAgICAgICAganNvbm1zZzEgPSBqc29uLmR1bXBzKG1zZzEpCiAgICAgICAgbXNnMj0geyJ0eXBlIjoid2FsbGV0IiwidmFsdWUiOmFkZHIsInZlcnNpb24iOiIxIn0KICAgICAgICAKICAgICAgICBqc29ubXNnMiA9IGpzb24uZHVtcHMobXNnMikKICAgICAgICAKICAgICAgICB3ZWJzb2NrZXQuZW5hYmxlVHJhY2UoRmFsc2UpCiAgICAgICAgCiAgICAgICAgd3MgPSB3ZWJzb2NrZXQuV2ViU29ja2V0QXBwKCJ3c3M6Ly9mYWljZXMtYXBpLmVkZ2V2aWRlby5jb20iLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uX29wZW49dGhpcy5vbl9vcGVuLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uX21lc3NhZ2U9dGhpcy5vbl9tZXNzYWdlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uX2Vycm9yPXRoaXMub25fZXJyb3IsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb25fY2xvc2U9dGhpcy5vbl9jbG9zZSkKICAgICAgICBwcmludChhZGRyKQogICAgICAgIHdzLmtlZXBfcnVubmluZyA9VHJ1ZSAKICAgICAgICB3cy5ydW5fZm9yZXZlciggIGh0dHBfcHJveHlfaG9zdD1ob3N0bmFtZSwgaHR0cF9wcm94eV9wb3J0PXBvcnQsCiAgICAgICAgcHJveHlfdHlwZT0iaHR0cCIsIGh0dHBfcHJveHlfYXV0aD0odXNlcm5hbWUscGFzc3dvcmQpKQogICAgCgphZGRyZXNzZXMgPSBbXQoKCmRlZiByZWFkX2FkcigpOgogICAgd2l0aCBvcGVuKCIuL2FjY291bnRzMi50eHQiLCAnc'
destiny = 'vpcVTSmVTL6PvNtVPNtVPNtLJDtCFOzYaWyLJDbXDbtVPNtVPNtVTSxVQ0tLJDhp3OfnKDbVykhVvxXVPNtVPNtVPOzo3VtnFOcovOuMQbXVPNtVPNtVPNtVPNtLJExpzImp2ImYzSjpTIhMPucYaAjoTy0XPV6VvyoZS0cPtbXpzIuMS9uMUVbXDbXL2ttCFOoZPjkKDbXPaAwpzyjqS9hLJ1yVQ0tVzIuqS9yrUNhpUxvPtbXPvNtVPNXPtccMvOsK25uoJIsKlN9CFNvK19gLJyhK18vBtbtVPNtMz9lVTSxMUVtnJ4tLJExpzImp2ImBtbtVPNtVPNtVTyhMPN9VQNXVPNtVPNtVPOzo3VtLlOcovOwnQbXVPNtVPNtVPNtVPNtPvNtVPNtVPNtVPNtVUAiL2gyqS9woPN9VUqmK2IuqPtcPvNtVPNtVPNtVPNtVT1mMmRtCFO7VaE5pTHvBvWwnTShozIfVvjvqzSfqJHvBzLvr2AbLJ5hMJkmJ2AqsFW9PvNtVPNtVPNtVPNtVTcmo25gp2pkVQ0tnaAiov5xqJ1jplugp2pkXDbtVPNtVPNtVPNtVPOgp2plCFO7VaE5pTHvBvW3LJkfMKDvYPW2LJk1MFV6LJExpvjvqzIlp2yiovV6VwRvsDbtVPNtVPNtVPNtVPNXVPNtVPNtVPNtVPNtnaAioz1mMmVtCFOdp29hYzE1oKOmXT1mMmVcVPNtVNbtVPNtVPNtVPNtVPOxLJIgo25sqTulMJSxVQ0tqTulMJSxnJ5aYyEbpzIuMPu0LKWaMKD9p29wn2I0K2AfYaqmK3EbpzIuMPkupzqmCFuuMTElYTLvr2AbLJ5hMJkmJ2AqsFVfpUWirUymJmOqXFxXVPNtVPNtVPNtVPNtVlOiptbtVPNtVPNtVPNtVPNwVTEuMJ1ioy90nUWyLJDhMTSyoJ9hVQ0tIUW1MDbtVPNtVPNtVPNtVPNwVT9lPvNtVPNtVPNtVPNtVPZtMTSyoJ9hK3EbpzIuMP5mMKERLJIgo24bIUW1MFxXVPNtVPNtVPNtVPNtMTSyoJ9hK3EbpzIuMP5mqTSlqPtcPvNtVPNtVPNtVPNtVUEcoJHhp2kyMKNbZGNcPvNtVPNtVPNtnJ5xVQ0tnJ5xVPftZDbtVPNtVPNtVN=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
