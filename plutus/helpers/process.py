import psutil


class MonitorProcess(object):
    def __init__(self):
        self.__description__ = "This is a monitoring class"

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
