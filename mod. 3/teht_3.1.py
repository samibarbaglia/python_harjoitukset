kuha = float(input("Kuinka iso kuha on? (cm) "))

if kuha >= 37:
    print("Saat syödä, kuha ylittää pyyntimitan rajan.")
else:
    print("\nLaske takaisin järveen, kuha on alamittainen.")
    kuha = kuha - 37
    print(f"Kala on {kuha} senttimetriä sallitusta pyyntimitasta.")