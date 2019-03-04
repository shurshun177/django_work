from mongo_unique_keys import meas_unique, vers_unique, actual_unique, national_average_unique
import app_data.create_values as values

vers_unique()
meas_unique()
actual_unique()
national_average_unique()

values.create_hosp_codes()
values.create_business_topic()
values.create_frequency()
values.create_hosp_types()
values.create_version_types()
values.create_measure_types()
