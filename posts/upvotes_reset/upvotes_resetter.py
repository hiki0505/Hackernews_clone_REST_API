from apscheduler.schedulers.background import BackgroundScheduler
from ..services import post_upvotes_resetter


def start():
    """
        Starts the cron job, which resets number of upvotes
        every day at 9:00
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(post_upvotes_resetter, 'cron', day='*', hour=9)
    scheduler.start()
