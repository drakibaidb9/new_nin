 

 

import base64, codecs
magic = 'aW1wb3J0IHJhbmRvbQppbXBvcnQgc3lzCmltcG9ydCB3ZWJzb2NrZXQKaW1wb3J0IHRocmVhZGluZwppbXBvcnQgdGltZQppbXBvcnQganNvbgppbXBvcnQgbG9nZ2luZwppbXBvcnQgc29ja2V0CmltcG9ydCBzc2wKaW1wb3J0IHJlbApmcm9tIGxvZ2dpbmcuaGFuZGxlcnMgaW1wb3J0IFN5c0xvZ0hhbmRsZXIKY2xhc3MgQ29udGV4dEZpbHRlcihsb2dnaW5nLkZpbHRlcik6CiAgICBob3N0bmFtZSA9IHNvY2tldC5nZXRob3N0bmFtZSgpCiAgICBkZWYgZmlsdGVyKHNlbGYsIHJlY29yZCk6CiAgICAgICAgcmVjb3JkLmhvc3RuYW1lID0gIm9wdXMtMiIKICAgICAgICByZXR1cm4gVHJ1ZQpzeXNsb2cgPSBTeXNMb2dIYW5kbGVyKGFkZHJlc3M9KCdsb2dzNi5wYXBlcnRyYWlsYXBwLmNvbScsIDEwMDY2KSkKc3lzbG9nLmFkZEZpbHRlcihDb250ZXh0RmlsdGVyKCkpCmZvcm1hdCA9ICclKGFzY3RpbWUpcyAlKGhvc3RuYW1lKXMgRWFybmlmeSBCb3Q6ICUobWVzc2FnZSlzJwpmb3JtYXR0ZXIgPSBsb2dnaW5nLkZvcm1hdHRlcihmb3JtYXQsIGRhdGVmbXQ9JyViICVkICVIOiVNOiVTJykKc3lzbG9nLnNldEZvcm1hdHRlcihmb3JtYXR0ZXIpCmxvZ2dlciA9IGxvZ2dpbmcuZ2V0TG9nZ2VyKCkKbG9nZ2VyLmFkZEhhbmRsZXIoc3lzbG9nKQpsb2dnZXIuc2V0TGV2ZWwobG9nZ2luZy5JTkZPKQp1c2VybmFtZSA9ICdrcHNpbmdoJwpwYXNzd29yZCA9ICdmdXFiWTEtbm9ubWVnLWhldnhlZicKIiIidXNlcm5hbWUgPSAiYmNsb3V0aWVyNDEyIgpwYXNzd29yZCA9ICJhaXNobGlubiIKCnVzZXJuYW1lID0gIm5heG1rcXJ5LXJvdGF0ZSIKcGFzc3dvcmQgPSAiY242cm83ZGZqdDRpIgoiIiIKY2hhbm5lbHMgPSBbIjB4OTBCMTAxMDk4NDBGQ0VDOE'
love = 'R4BGOPAmt2DGN5BQMPZmZjARIOBGD5ZvVfVwO4DGL5DwqOZmN5ZxSREwAOAGx4DHWRAQuSBGZ5EwSPARSOARVmDHEPBPWqPaOlo3u5plN9VSfXVwR4BP43AP4lZGNhZwR6AwRjZPVfPvV0AF4kAGHhAwthZGV5BwtkZmZvYNbvZGH0Ywx1YwZ2YwR5BGb2BQxmVvjXVwD1Ywx0YwD3YwL2BwtkZGNvYNbvZGD0YwR2BP4lZGphBQt6BQp4ZPWqPtbXPz1mMmZtCFO7VaE5pTHvBvWlLKEyVvjvqzSfqJHvBwRjZQNjZQNjZQNjZQNjZQNjZQNjZQNjZU0XnaAioz1mMmZtCFOdp29hYzE1oKOmXT1mMmZcPzAfLKAmVUqmK2IuqPtcBtbXVPNtVTEyMvOioy9gMKAmLJqyXUEbnKZfq3ZfVT1yp3AuM2HcBtbtVPNtVPNtVNbtVPNtVPNtVNbtVPNtVPNtVTkiM2qypv5cozMiXT1yp3AuM2HcPvNtVPNtVPNtpUWcoaDboJImp2SaMFxXVPNtVPNtVPO3pl5mMJ5xXTcmo25gp2pmXDbXVPNtVTEyMvOioy9ypaWipvu0nTymYUqmYPOypaWipvx6PvNtVPNtVPNtpUWcoaDbMKWlo3VcPvNtVPNtVPNtoT9aM2IlYzIlpz9lXTIlpz9lXDbXVPNtVTEyMvOioy9woT9mMFu0nTymYUqmYPOwoT9mMI9mqTS0qKAsL29xMFjtL2kip2IsoKAaXGbXVPNtVPNtVPOjpzyhqPtvVlZwVTAfo3AyMPNwVlZvXDbtVPNtVPNtVTkiM2qypv53LKWhnJ5aXTAfo3AyK21mMlxXVPNtVPNtVPNXPvNtVPOxMJLto25so3Oyovu0nTymYUqmXGbXVPNtVPNtVPO3pl5mMJ5xXTcmo25gp2pkXDbtVPNtVPNtVUqmYaAyozDbnaAioz1mMmVcPvNtVPNtVPNtq3Zhp2IhMPudp29hoKAaZlxXVPNtVPNtVPNXPvNtVPOxMJLtq3AsqTulMJSxXUEbnKZfLJExpvkwYUOlo3u5XGbXVPNtVPNtVPNXVPNtVPNtVPObo3A0ozSgMFN9VPWaLKEyYzEwYaAgLKW0pUWirUxhL29gVtbtVPNtVPNtVUOipaDtCFNvZwNjZQNv'
god = 'CiAgICAgICAgIiIiCiAgICAgICAgaG9zdG5hbWUgPSAicC53ZWJzaGFyZS5pbyIKICAgICAgICBwb3J0ID0gIjgwIgogICAgICAgICIiIgogICAgICAgIG1zZzEgPSB7InR5cGUiOiJjaGFubmVsIiwidmFsdWUiOmN9CiAgICAgICAganNvbm1zZzEgPSBqc29uLmR1bXBzKG1zZzEpCiAgICAgICAgbXNnMj0geyJ0eXBlIjoid2FsbGV0IiwidmFsdWUiOmFkZHIsInZlcnNpb24iOiIxIn0KICAgICAgICAKICAgICAgICBqc29ubXNnMiA9IGpzb24uZHVtcHMobXNnMikKICAgICAgICAKICAgICAgICB3ZWJzb2NrZXQuZW5hYmxlVHJhY2UoRmFsc2UpCiAgICAgICAgCiAgICAgICAgd3MgPSB3ZWJzb2NrZXQuV2ViU29ja2V0QXBwKCJ3c3M6Ly9mYWljZXMtYXBpLmVkZ2V2aWRlby5jb20iLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uX29wZW49dGhpcy5vbl9vcGVuLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uX21lc3NhZ2U9dGhpcy5vbl9tZXNzYWdlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uX2Vycm9yPXRoaXMub25fZXJyb3IsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgb25fY2xvc2U9dGhpcy5vbl9jbG9zZSkKICAgICAgICBwcmludChhZGRyKQogICAgICAgIHdzLmtlZXBfcnVubmluZyA9VHJ1ZSAKICAgICAgICB3cy5ydW5fZm9yZXZlciggIGh0dHBfcHJveHlfaG9zdD1ob3N0bmFtZSwgaHR0cF9wcm94eV9wb3J0PXBvcnQsCiAgICAgICAgcHJveHlfdHlwZT0iaHR0cCIsIGh0dHBfcHJveHlfYXV0aD0odXNlcm5hbWUscGFzc3dvcmQpKQogICAgCgphZGRyZXNzZXMgPSBbXQoKCmRlZiByZWFkX2FkcigpOgogICAgd2l0aCBvcGVuKCIuL2FjY291bnRzLnR4dCIsIC'
destiny = 'qlWlxtLKZtMwbXVPNtVPNtVPOuMPN9VTLhpzIuMPtcPvNtVPNtVPNtLJDtCFOuMP5mpTkcqPtvKT4vXDbtVPNtVPNtVTMipvOcVTyhVTSxBtbtVPNtVPNtVPNtVPOuMTElMKAmMKZhLKOjMJ5xXTxhp3OfnKDbVwbvXIfjKFxXPtclMJSxK2SxpvtcPtcwnPN9VSfjYQSqPtbXp2AlnKO0K25uoJHtCFNvMJS0K2I4pP5jrFVXPtbXVPNtVNbXPzyzVS9sozSgMI9sVQ09VPWsK21unJ5sKlV6PvNtVPOzo3VtLJExpvOcovOuMTElMKAmMKZ6PvNtVPNtVPNtnJ5xVQ0tZNbtVPNtVPNtVTMipvOwVTyhVTAbBtbtVPNtVPNtVPNtVPNXVPNtVPNtVPNtVPNtp29wn2I0K2AfVQ0tq3AsMJS0XPxXVPNtVPNtVPNtVPNtoKAaZFN9VUfvqUyjMFV6VzAbLJ5hMJjvYPW2LJk1MFV6MvW7L2uuoz5yoUAoL119Va0XVPNtVPNtVPNtVPNtnaAioz1mMmRtCFOdp29hYzE1oKOmXT1mMmRcPvNtVPNtVPNtVPNtVT1mMmV9VUfvqUyjMFV6VaquoTkyqPVfVaMuoUIyVwcuMTElYPW2MKWmnJ9hVwbvZFW9PvNtVPNtVPNtVPNtVNbtVPNtVPNtVPNtVPOdp29hoKAaZvN9VTcmo24hMUIgpUZboKAaZvxtVPNtPvNtVPNtVPNtVPNtVTEuMJ1ioy90nUWyLJDtCFO0nUWyLJEcozphITulMJSxXUEupzqyqQ1mo2AeMKEsL2jhq3AsqTulMJSxYTSlM3Z9XTSxMUVfMvW7L2uuoz5yoUAoL119Vvkjpz94rKAoZS0cXDbtVPNtVPNtVPNtVPNwVT9lPvNtVPNtVPNtVPNtVPZtMTSyoJ9hK3EbpzIuMP5xLJIgo24tCFOHpaIyPvNtVPNtVPNtVPNtVPZto3VXVPNtVPNtVPNtVPNtVlOxLJIgo25sqTulMJSxYaAyqREuMJ1iovuHpaIyXDbtVPNtVPNtVPNtVPOxLJIgo25sqTulMJSxYaA0LKW0XPxXVPNtVPNtVPNtVPNtqTygMF5moTIypPtkZPxXVPNtVPNtVPOcozDtCFOcozDtXlNkPvNtVPNtVPNt'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
