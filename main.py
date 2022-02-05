import extract
import transform
import pandas as pd
from sqlalchemy import create_engine

dates = ["1/1/1991", "12/1/2000"]

if __name__ == "__main__":
    user_path = extract.get_path()
    lines, header = extract.load(user_path)
    data_dict = transform.lines_to_dict(lines)
    # print(
    #     f"Xref: {len(data_dict['Xref'])}, Yref: {len(data_dict['Yref'])}, Value: {len(data_dict['Value'])}")
    # print(data_dict['Value'][0:20])
    # print(data_dict['Value'][-20:])

    dates_long = transform.datelist(dates)
    data_dict.update({'Date': dates_long})
    # print(f"Xref: {len(data_dict['Xref'])}, Yref: {len(data_dict['Yref'])},
    #       Value: {len(data_dict['Value']}), Date: {len(data_dict['Date'])}")

    val_df = pd.DataFrame.from_dict(data_dict)

    engine = create_engine('sqlite:///data/precip_data.db', echo=True)
    with engine.begin() as connection:
        sqlite_table = "Precipitation Grid Values"
        val_df.to_sql(sqlite_table, connection, if_exists='fail')
