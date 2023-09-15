# Paracetamol/Panadol/Tylenol Dosing Advisor

def calculate_dose(weight, time, last_total_dose):
    """This function calculates the dose of paracetamol
    to be given to the patient.

    :param weight: int, Patient weight in kilograms.
    :param time: int, Hours passed since last time the medicine is taken.
    :param last_total_dose: int, Total dose of medicine taken this day.
    :return: int, Dose amount to be taken.
    """
    if time < 6:
        return 0
    amount = weight * 15
    if time >= 6 and amount <= (4000 - last_total_dose):
        return amount
    elif time >= 6 and amount > (4000 - last_total_dose):
        return (4000 - last_total_dose)


def main():
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_dose_24h = int(input("The total dose for the last 24 hours (mg): "))
    print("The amount of Parasetamol to give to the patient:", calculate_dose(weight, time, total_dose_24h))

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
    main()
