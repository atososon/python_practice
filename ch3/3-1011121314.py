e2f = {"dog":"chien","cat":"chat","walrus":"morse"}
print(e2f)
print(e2f["walrus"])

f2e = {v: k for k, v in e2f.items()}
print(f2e)
print(f2e["chien"])
print(set(e2f))