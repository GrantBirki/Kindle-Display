from ImageProducer import main, logging_data, scp_send, add_time

timezone = 'pst'
environment = 'prod'
bus_numbers = ['62', '31']
bus_urls = ['http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/1_18270.json?key=', 'http://api.pugetsound.onebusaway.org/api/where/arrivals-and-departures-for-stop/1_18250.json?key=']
main(environment, timezone, bus_numbers, bus_urls)