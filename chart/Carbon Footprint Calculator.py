# Konstanta Electricity
import numpy as np
import matplotlib.pyplot as plt

const_electricity = {"electricity": 0.794}  # kg co2

# Konstanta Travel
const_travel = {"car": 0.27, "motorbike": 0.15, "bus": 0.08, "train": 0.04}

# Konstanta Food
const_food = {"beef": 27.0,  # kg co2
              "chicken": 6.9,  # kg co2
              "fish": 6.1,  # kg co2
              "rice": 2.7,  # kg co2
              "vegetables": 2.0,  # kg co2
              "milk": 1.9,  # kg co2
              "fruit": 1.1}  # kg co2

# Konstanta Fashion
const_fashion = {"shirt": (13 + 12) / 2,  # kg CO2eq per product
                 "tshirt": (7 + 10 + 6) / 3,  # kg CO2eq per product
                 "jeans": 25,  # kg CO2eq per product
                 # kg CO2eq per product
                 "sweater": (28 + 26 + 31 + 56 + 12) / 5,
                 "coat": (89 + 39 + 25) / 3,  # kg CO2eq per product
                 "dress": (56 + 56 + 51) / 3,  # kg CO2eq per product
                 "shoes": (15 + 19 + 20) / 3}  # kg CO2eq per product

# Electricity Carbon Calculator


def electricity_calculator(electricity):
    kwh_buyr = int(input("Electricity usage pe month (kWh): "))
    orang_rumah = int(input("How many people are in your hobuyhold: "))
    result_electricity = (electricity * kwh_buyr)/orang_rumah
    return result_electricity

# Travel Carbon Calculator


def travel_calculator(car, motorbike, bus, train):
    km_car = int(input("How many km do you travel with car in month: "))
    km_motorbike = int(
        input("How many km do you travel with motorbike in month: "))
    km_bus = int(input("How many km do you travel with bus in month: "))
    km_train = int(input("How many km do you travel with train in month: "))
    carbon_car = km_car * car
    carbon_motorbike = km_motorbike * motorbike
    carbon_bus = km_bus * bus
    carbon_train = km_train * train
    result_travel = carbon_car + carbon_motorbike + carbon_bus + carbon_train
    return result_travel

# Fashion Carbon Calculator


def food_calculator(beef, chicken, fish, rice, vegetables, milk, fruit):
    kg_beef = int(input("How many kg do you eat beef in month: "))
    kg_chicken = int(input("How many kg do you eat chicken in month: "))
    kg_fish = int(input("How many kg do you eat fish in month: "))
    kg_rice = int(input("How many kg do you eat rice in month: "))
    kg_vegetables = int(input("How many kg do you vegetables beef in month: "))
    kg_milk = int(input("How many liter do you drink milk in month: "))
    kg_fruit = int(input("How many kg do you eat fruit in month: "))
    carbon_beef = kg_beef * beef
    carbon_chicken = kg_chicken * chicken
    carbon_fish = kg_fish * fish
    carbon_rice = kg_rice * rice
    carbon_vegetables = kg_vegetables * vegetables
    carbon_milk = kg_milk * milk
    carbon_fruit = kg_fruit * fruit
    result_food = carbon_beef + carbon_chicken + carbon_fish + \
        carbon_rice + carbon_vegetables + carbon_milk + carbon_fruit
    return result_food

# Fashion Carbon Calculator


def fashion_calculator(shirt, tshirt, jeans, sweater, coat, dress, shoes):
    t_shirt = int(input("How many shirts do you buy in a month: "))
    t_tshirt = int(input("How many t-shirts do you buy in a month: "))
    t_jeans = int(input("How many jeans do you buy in a month: "))
    t_sweater = int(input("How many sweater do you buy in a month: "))
    t_coat = int(input("How many coat do you buy in a month: "))
    t_dress = int(input("How many dress do you buy in a month: "))
    t_shoes = int(input("How many shoes do you buy in a month: "))
    carbon_shirt = t_shirt * shirt
    carbon_tshirt = t_tshirt * tshirt
    carbon_jeans = t_jeans * jeans
    carbon_sweater = t_sweater * sweater
    carbon_coat = t_coat * coat
    carbon_dress = t_dress * dress
    carbon_shoes = t_shoes * shoes
    result_fashion = carbon_shirt + carbon_tshirt + carbon_jeans + \
        carbon_sweater + carbon_coat + carbon_dress + carbon_shoes
    return result_fashion


def drawBarChart():

    # creating the dataset
    labels = np.array(['Electricity', 'travel', 'Food', 'Fashion'])
    # yang 23 diisi fashion nanti, yang 16 bisa diisi food
    sizes = np.array([carbon_electricity, carbon_travel,
                     carbon_fashion, carbon_food])

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(labels, sizes,
            width=0.4)

    plt.xlabel("Carbon Uses")
    plt.ylabel("Amount Carbon in percent")
    plt.title("Carbon Footprint Calculator")
    # plt.show()


def drawPieChart():
    labels = np.array(['Electricity', 'travel', 'Food', 'Fashion'])
    # yang 23 diisi fashion nanti, yang 16 bisa diisi food
    sizes = np.array([carbon_electricity, carbon_travel,
                     carbon_fashion, carbon_food])

    porcent = 100.*sizes/float(sizes.sum())

    patches, texts = plt.pie(sizes, startangle=90, radius=1.2)
    labels = ['{0} - {1:1.2f} %'.format(i, j) for i, j in zip(labels, porcent)]

    sort_legend = True
    if sort_legend:
        patches, labels, dummy = zip(*sorted(zip(patches, labels, sizes),
                                             key=lambda x: x[2],
                                             reverse=True))

    plt.legend(patches, labels, loc='center left', bbox_to_anchor=(-0.1, 1.),
               fontsize=8)

    plt.savefig('piechart.png', bbox_inches='tight')
    # plt.show()


# Result
carbon_electricity = electricity_calculator(const_electricity["electricity"])
carbon_travel = travel_calculator(
    const_travel["car"], const_travel["motorbike"], const_travel["bus"], const_travel["train"])
carbon_food = food_calculator(
    const_food["beef"], const_food["chicken"], const_food["fish"], const_food["rice"], const_food["vegetables"], const_food["milk"], const_food["fruit"])
carbon_fashion = fashion_calculator(
    const_fashion["shirt"], const_fashion["tshirt"], const_fashion["jeans"], const_fashion["sweater"], const_fashion["coat"], const_fashion["dress"], const_fashion["shoes"])
total_carbon = carbon_electricity + carbon_travel + carbon_food + carbon_fashion

print("Your carbon emission from electricity: ", carbon_electricity)
print("Your carbon emission from travel: ", carbon_travel)
print("Your carbon emission from food: ", carbon_food)
print("Your carbon emission from fashion: ", carbon_fashion)
print("Total carbon you produce this month: ", total_carbon)

# Visualisasi
drawPieChart()
drawBarChart()

plt.show()
