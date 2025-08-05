import weather as w
import weather_querry as querry

process = [[1,3],[2,8],[0,5],[3,6]]

w.print_date_wether()
# time, wait_time = scheduler_algorithm.FCFS(process)

# print(f'{time} and {wait_time}')


# traffic_sql.create_traffic_table()
# traffic_sql.insert_train()
# traffic_sql.show_traffic_table()


# w.print_date_wether()

querry.create_tables()

def job():
    data = w.get_wether_data()
    # querry.