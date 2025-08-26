from zoneinfo import ZoneInfo

from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

import configuration
import scheduling
import service
import util
from configuration.logging_configuration import logger as log
from scheduling import ca_update_scheduler_bean, certificate_update_scheduler_bean

[log.info(f"Init {_module}") for _module in [configuration,
                                             scheduling,
                                             service,
                                             util]]

if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone=ZoneInfo("UTC"))
    cron_expr_every_minute = CronTrigger.from_crontab("* * * * *")
    scheduler.add_job(ca_update_scheduler_bean.schedule, cron_expr_every_minute)
    scheduler.add_job(certificate_update_scheduler_bean.schedule, cron_expr_every_minute)
    scheduler.start()
