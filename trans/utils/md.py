logger = logging.getLogger(__name__)

def save_final_md(translation):
    task = translation.task
    user = translation.user
    md_file_path = output_md_path(task.contest.slug, task.name, user)
    with open(md_file_path, 'w') as mdf:
        mdf.write(translation.get_latest_text())
    return md_file_path

# pdf file paths (excepting final pdf path)
def output_md_path(contest_slug, task_name, user):
    file_path = 'media/md/{}'.format(contest_slug)
    file_name = '{}-{}.pdf'.format(task_name, user.language_code)
    md_file_path = '{}/{}'.format(file_path, file_name)
    os.makedirs(file_path, exist_ok=True)
    return md_file_path
