# determine the award a person competing in a triathlon receives
# access the events of the triathalon and the minutes for each event
# calculate total time to complete the full event
# if the total time is under 100 minutes then awards are based on
#   at 100mins - provinicial colours
#   between 105-101mins - provincial half colours
#   between 110-106mins - provincial scroll
#   over 110mins - no award


swim_time = float(input("Please type in the contestant swim time (mins):  "))
cycle_time = float(input("Please type in the contestant cycle time (mins):  "))
run_time = float(input("Please type in the contestant run time (mins):  "))

total_triathlon_time = swim_time + cycle_time + run_time
print(f"Total time taken to complete the triathlon: {total_triathlon_time} mins")

if total_triathlon_time > 110:
    print("Contestant receives no awards")
elif total_triathlon_time > 105:
    print("Contestant receives Provincial Scroll")
elif total_triathlon_time > 100:
    print("Contestant receives Provincial Half Colours")
else:
    print("Contestant receives Provincial Colours")