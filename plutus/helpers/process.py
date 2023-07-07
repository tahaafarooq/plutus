import psutil
import systemd
import subprocess


class MonitorProcess(object):
    def __init__(self):
        self.__description__ = "This is a monitoring class"

    # get all systemd services running

    def get_all_services(self):
        manager = systemd.Manager()
        services = manager.list_units()

        return [service.UnitName for service in services if services.Type == 'service']

    # monitor the cronjob processes and dump
    @staticmethod
    def monitor_cronjobs():
        cron_processes = []
        output = []
        processes = psutil.process_iter(['name', 'cmdline'])

        for process in processes:
            name = process.info['name']
            cmdline = process.info['cmdline']

            if name == 'cron' or 'cron' in cmdline:
                cron_processes.append(process)

        if cron_processes:
            for process in cron_processes:
                data = f"[PID : {process.pid}] - [NAME : {process.info['name']}] - [CMD : {''.join(process.info['cmdline'])}]"
                output.append(data)

            return output
        else:
            return "NO CRONJOB FOUND"

    # monitor for all systemd services running
    def monitor_systemd(self):
        services = self.get_all_services()
        output = []
        errors = []

        for service_name in services:
            try:
                unit = systemd.Unit(service_name)
                unit.load()
                unit_state = unit.Unit.ActiveState
                
                data = f"[SERVICE] [{service_name}] : [SERVICE STATE] [{unit_state}]"
                output.append(data)
            except systemd.exceptions.SystemdException as e:
                data = f"ERROR RETRIEVING STATUS FOR SERVICE [{service_name}]"
                errors.append(data)

        return output

    # monitor binaries processes running
    def monitor_bin(self):
        command = ['ps', 'aux']
        results = []
        output = subprocess.check_output(command, universal_newlines=True)

        for line in output.splitlines()[1:]:
            fields = line.split()
            process_name = fields[10]
            binary_path = fields[11]

            data = {
                f"[{process_name}]": f"[{binary_path}]"
            }

            results.append(data)

        return results
# Get the list of running processes
processes = psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])

for process in processes:
    # Access process information
    pid = process.info['pid']
    name = process.info['name']
    cpu_percent = process.info['cpu_percent']
    memory_percent = process.info['memory_percent']
    
    print(f"Process ID: {pid}")
    print(f"Name: {name}")
    print(f"CPU Percent: {cpu_percent}%")
    print(f"Memory Percent: {memory_percent}%")
    print("---------------------------")
