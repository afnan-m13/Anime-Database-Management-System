import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from tkinter.font import Font
# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "animeuchiha"
}

def add_department():
    department_window = tk.Toplevel(root)
    department_window.title("Add Department")
    department_window.geometry("900x450")
    department_window.configure(bg="lemonchiffon1")
    times_font = Font(family="Times", size=12)

    def insert_department():
        Dname = department_name.get()
        Dgenres = department_genres.get()
        Doffice = department_office.get()
        DID = department_id.get()
        SID = department_manager.get()

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            sql_insert = "INSERT INTO department (dname, dgenres, doffice, did, sid) VALUES (%s, %s, %s, %s, %s)"
            values = (Dname, Dgenres, Doffice, DID, SID)

            cursor.execute(sql_insert, values)
            connection.commit()
            cursor.close()
            connection.close()

            messagebox.showinfo("Success", "Department added successfully!")
            department_window.destroy()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add department: {str(error)}")


    label_department_name = tk.Label(department_window, text="Department Name:", font=times_font,bg="lemonchiffon1")
    label_department_name.grid(row=0, column=0)
    department_name = tk.Entry(department_window, width=40)
    department_name.grid(row=0, column=1)

    label_department_genres = tk.Label(department_window, text="Department Genres:", font=times_font,bg="lemonchiffon1")
    label_department_genres.grid(row=1, column=0,sticky="w")
    department_genres = tk.Entry(department_window,width=40)
    department_genres.grid(row=1, column=1,sticky="w")

    label_department_office = tk.Label(department_window, text="Department Office:", font=times_font,bg="lemonchiffon1")
    label_department_office.grid(row=2, column=0)
    department_office = tk.Entry(department_window,width=40)
    department_office.grid(row=2, column=1)

    label_department_id = tk.Label(department_window, text="Department ID:", font=times_font,bg="lemonchiffon1")
    label_department_id.grid(row=3, column=0)
    department_id = tk.Entry(department_window,width=40)
    department_id.grid(row=3, column=1)

    label_department_manager = tk.Label(department_window, text="Department Manager:", font=times_font,bg="lemonchiffon1")
    label_department_manager.grid(row=4, column=0)
    department_manager = tk.Entry(department_window,width=40)
    department_manager.grid(row=4, column=1)

    button_insert_department = tk.Button(department_window, text="Add Department", font=times_font,bg="lightgoldenrod1", command=insert_department)
    button_insert_department.grid(row=5, column=1)

def add_anime_projects():
    anime_projects_window = tk.Toplevel(root)
    anime_projects_window.title("Add Anime Project")
    anime_projects_window.geometry("900x450")
    anime_projects_window.configure(bg="lemonchiffon1")

    def insert_anime_projects():
        Atitle = anime_title.get()
        Acode = anime_code.get()
        Agenres = anime_genres.get()
        Adirector = anime_director.get()
        Adescripition = anime_descripition.get()
        writerDesc = anime_writerdesc.get()
        ADID = anime_department_id.get()

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            sql_insert = "INSERT INTO anime_projects (atitle, acode, agenres, adirector, adescripition, writerdesc, adid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (Atitle, Acode, Agenres, Adirector, Adescripition, writerDesc, ADID)

            cursor.execute(sql_insert, values)
            connection.commit()
            cursor.close()
            connection.close()

            messagebox.showinfo("Success", "Anime project added successfully!")
            anime_projects_window.destroy()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add anime project: {str(error)}")

    label_anime_title = tk.Label(anime_projects_window, text="Anime Title:",font=times_font,bg="lemonchiffon1")
    label_anime_title.grid(row=0, column=0)
    anime_title = tk.Entry(anime_projects_window,width=40)
    anime_title.grid(row=0, column=1)

    label_anime_code = tk.Label(anime_projects_window, text="Anime Code:",font=times_font,bg="lemonchiffon1")
    label_anime_code.grid(row=1, column=0)
    anime_code = tk.Entry(anime_projects_window,width=40)
    anime_code.grid(row=1, column=1)

    label_anime_genres = tk.Label(anime_projects_window, text="Anime Genres:",font=times_font,bg="lemonchiffon1")
    label_anime_genres.grid(row=2, column=0)
    anime_genres = tk.Entry(anime_projects_window,width=40)
    anime_genres.grid(row=2, column=1)

    label_anime_director = tk.Label(anime_projects_window,text="Anime Director:",font=times_font,bg="lemonchiffon1")
    label_anime_director.grid(row=3, column=0)
    anime_director = tk.Entry(anime_projects_window,width=40)
    anime_director.grid(row=3, column=1)

    label_anime_descripition = tk.Label(anime_projects_window, text="Anime Descripition:",font=times_font,bg="lemonchiffon1")
    label_anime_descripition.grid(row=4, column=0)
    anime_descripition = tk.Entry(anime_projects_window,width=40)
    anime_descripition.grid(row=4, column=1)

    label_anime_writerdesc = tk.Label(anime_projects_window, text="Anime writer:",font=times_font,bg="lemonchiffon1")
    label_anime_writerdesc.grid(row=5, column=0)
    anime_writerdesc = tk.Entry(anime_projects_window,width=40)
    anime_writerdesc.grid(row=5, column=1)

    label_anime_department_id = tk.Label(anime_projects_window, text="Department ID:",font=times_font,bg="lemonchiffon1")
    label_anime_department_id.grid(row=6, column=0)
    anime_department_id = tk.Entry(anime_projects_window,width=40)
    anime_department_id.grid(row=6, column=1)

    button_insert_anime_project = tk.Button(anime_projects_window, text="Add Anime Project",font=times_font,bg="lightgoldenrod1", command=insert_anime_projects)
    button_insert_anime_project.grid(row=7, column=1)

def addStaffmember():
    staff_window = tk.Toplevel(root)
    staff_window.title("Add Staff Member")
    staff_window.geometry("400x300")
    staff_window.configure(bg="lemonchiffon1")
    times_font = Font(family="Times", size=12)

    def insert_staff_member():
        SID = staff_id.get()
        Fname = first_name.get()
        Lname = last_name.get()
        S_job = job_title.get()
        De_DID = department_number.get()

        # Insert the staff member into the database
        sql_insert = "INSERT INTO stuffmembers VALUES (%s, %s, %s, %s, %s)"
        values = (S_job, Fname, Lname, SID, De_DID)
        
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(sql_insert, values)
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Staff member added successfully!")
            staff_window.destroy()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add staff member: {str(error)}")

    label_staff_id = tk.Label(staff_window, text="Staff Member ID:", font=times_font,bg="lemonchiffon1")
    label_staff_id.grid(row=0, column=0, padx=10, pady=10)
    staff_id = tk.Entry(staff_window, width=30)
    staff_id.grid(row=0, column=1, padx=10, pady=10)

    label_first_name = tk.Label(staff_window, text="First Name:", font=times_font,bg="lemonchiffon1")
    label_first_name.grid(row=1, column=0, padx=10, pady=10)
    first_name = tk.Entry(staff_window, width=30)
    first_name.grid(row=1, column=1, padx=10, pady=10)

    label_last_name = tk.Label(staff_window, text="Last Name:", font=times_font,bg="lemonchiffon1")
    label_last_name.grid(row=2, column=0, padx=10, pady=10)
    last_name = tk.Entry(staff_window, width=30)
    last_name.grid(row=2, column=1, padx=10, pady=10)

    label_job_title = tk.Label(staff_window, text="Job Title:", font=times_font,bg="lemonchiffon1")
    label_job_title.grid(row=3, column=0, padx=10, pady=10)
    job_title = tk.Entry(staff_window, width=30)
    job_title.grid(row=3, column=1, padx=10, pady=10)

    label_department_number = tk.Label(staff_window, text="Department Number:", font=times_font,bg="lemonchiffon1")
    label_department_number.grid(row=4, column=0, padx=10, pady=10)
    department_number = tk.Entry(staff_window, width=30)
    department_number.grid(row=4, column=1, padx=10, pady=10)

    button_insert_staff_member = tk.Button(staff_window, text="Add Staff Member", font=times_font,bg="lightgoldenrod1", command=insert_staff_member)
    button_insert_staff_member.grid(row=5, column=1, padx=10, pady=10)

def addStaffVoiceActor():
    voice_actor_window = tk.Toplevel(root)
    voice_actor_window.title("Add Staff Voice Actor")
    voice_actor_window.geometry("400x400")
    voice_actor_window.configure(bg="lemonchiffon1")
    times_font = Font(family="Times", size=12)

    def insert_staff_voice_actor():
        SID = staff_id.get()
        Fname = first_name.get()
        Lname = last_name.get()
        S_job = job_title.get()
        De_DID = department_number.get()
        roles = prominent_roles.get()
        Vdate = start_date.get()
        Vrange = voice_range.get()

        # Insert the staff member into the database
        sql_insert_staff = "INSERT INTO stuffmembers VALUES (%s, %s, %s, %s, %s)"
        values_staff = (S_job, Fname, Lname, SID, De_DID)

        # Insert the voice actor into the database
        sql_insert_voice_actor = "INSERT INTO voiceactor VALUES (%s, %s, %s, %s)"
        values_voice_actor = (SID, roles, Vdate, Vrange)

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(sql_insert_staff, values_staff)
            cursor.execute(sql_insert_voice_actor, values_voice_actor)
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Staff voice actor added successfully!")
            voice_actor_window.destroy()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add staff voice actor: {str(error)}")

    label_staff_id = tk.Label(voice_actor_window, text="Staff Member ID:", font=times_font,bg="lemonchiffon1")
    label_staff_id.grid(row=0, column=0, padx=10, pady=10)
    staff_id = tk.Entry(voice_actor_window, width=30)
    staff_id.grid(row=0, column=1, padx=10, pady=10)

    label_first_name = tk.Label(voice_actor_window, text="First Name:", font=times_font,bg="lemonchiffon1")
    label_first_name.grid(row=1, column=0, padx=10, pady=10)
    first_name = tk.Entry(voice_actor_window, width=30)
    first_name.grid(row=1, column=1, padx=10, pady=10)

    label_last_name = tk.Label(voice_actor_window, text="Last Name:", font=times_font,bg="lemonchiffon1")
    label_last_name.grid(row=2, column=0, padx=10, pady=10)
    last_name = tk.Entry(voice_actor_window, width=30)
    last_name.grid(row=2, column=1, padx=10, pady=10)

    label_job_title = tk.Label(voice_actor_window, text="Job Title:", font=times_font,bg="lemonchiffon1")
    label_job_title.grid(row=3, column=0, padx=10, pady=10)
    job_title = tk.Entry(voice_actor_window, width=30)
    job_title.grid(row=3, column=1, padx=10, pady=10)

    label_department_number = tk.Label(voice_actor_window, text="Department Number:", font=times_font,bg="lemonchiffon1")
    label_department_number.grid(row=4, column=0, padx=10, pady=10)
    department_number = tk.Entry(voice_actor_window, width=30)
    department_number.grid(row=4, column=1, padx=10, pady=10)

    label_prominent_roles = tk.Label(voice_actor_window, text="Prominent Roles:", font=times_font,bg="lemonchiffon1")
    label_prominent_roles.grid(row=5, column=0, padx=10, pady=10)
    prominent_roles = tk.Entry(voice_actor_window, width=30)
    prominent_roles.grid(row=5, column=1, padx=10, pady=10)

    label_start_date = tk.Label(voice_actor_window, text="Start Date:", font=times_font,bg="lemonchiffon1")
    label_start_date.grid(row=6, column=0, padx=10, pady=10)
    start_date = tk.Entry(voice_actor_window, width=30)
    start_date.grid(row=6, column=1, padx=10, pady=10)

    label_voice_range = tk.Label(voice_actor_window, text="Voice Range:", font=times_font,bg="lemonchiffon1")
    label_voice_range.grid(row=7, column=0, padx=10, pady=10)
    voice_range = tk.Entry(voice_actor_window, width=30)
    voice_range.grid(row=7, column=1, padx=10, pady=10)

    button_insert_staff_voice_actor = tk.Button(voice_actor_window, text="Add Staff Voice Actor", font=times_font,bg="lightgoldenrod1", command=insert_staff_voice_actor)
    button_insert_staff_voice_actor.grid(row=8, column=1, padx=10, pady=10)

def addStaffAnimation():
    animation_window = tk.Toplevel(root)
    animation_window.title("Add Staff Animation")
    animation_window.geometry("400x400")
    animation_window.configure(bg="lemonchiffon1")
    times_font = Font(family="Times", size=12)

    def insert_staff_animation():
        SID = staff_id.get()
        Fname = first_name.get()
        Lname = last_name.get()
        S_job = job_title.get()
        De_DID = department_number.get()
        astyle = animation_style.get()
        Date_joined = date_joined.get()
        Notableworks = notable_works.get()

        # Insert the staff member into the database
        sql_insert_staff = "INSERT INTO stuffmembers VALUES (%s, %s, %s, %s, %s)"
        values_staff = (S_job, Fname, Lname, SID, De_DID)

        # Insert the animation staff into the database
        sql_insert_animation = "INSERT INTO animation VALUES (%s, %s, %s, %s)"
        values_animation = (SID, astyle, Notableworks, Date_joined)

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(sql_insert_staff, values_staff)
            cursor.execute(sql_insert_animation, values_animation)
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Staff animation added successfully!")
            animation_window.destroy()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add staff animation: {str(error)}")

    label_staff_id = tk.Label(animation_window, text="Staff Member ID:", font=times_font,bg="lemonchiffon1")
    label_staff_id.grid(row=0, column=0, padx=10, pady=10)
    staff_id = tk.Entry(animation_window, width=30)
    staff_id.grid(row=0, column=1, padx=10, pady=10)

    label_first_name = tk.Label(animation_window, text="First Name:", font=times_font,bg="lemonchiffon1")
    label_first_name.grid(row=1, column=0, padx=10, pady=10)
    first_name = tk.Entry(animation_window, width=30)
    first_name.grid(row=1, column=1, padx=10, pady=10)

    label_last_name = tk.Label(animation_window, text="Last Name:", font=times_font,bg="lemonchiffon1")
    label_last_name.grid(row=2, column=0, padx=10, pady=10)
    last_name = tk.Entry(animation_window, width=30)
    last_name.grid(row=2, column=1, padx=10, pady=10)

    label_job_title = tk.Label(animation_window, text="Job Title:", font=times_font,bg="lemonchiffon1")
    label_job_title.grid(row=3, column=0, padx=10, pady=10)
    job_title = tk.Entry(animation_window, width=30)
    job_title.grid(row=3, column=1, padx=10, pady=10)

    label_department_number = tk.Label(animation_window, text="Department Number:", font=times_font,bg="lemonchiffon1")
    label_department_number.grid(row=4, column=0, padx=10, pady=10)
    department_number = tk.Entry(animation_window, width=30)
    department_number.grid(row=4, column=1, padx=10, pady=10)

    label_animation_style = tk.Label(animation_window, text="Animation Style:", font=times_font,bg="lemonchiffon1")
    label_animation_style.grid(row=5, column=0, padx=10, pady=10)
    animation_style = tk.Entry(animation_window, width=30)
    animation_style.grid(row=5, column=1, padx=10, pady=10)

    label_date_joined = tk.Label(animation_window, text="Date Joined:", font=times_font,bg="lemonchiffon1")
    label_date_joined.grid(row=6, column=0, padx=10, pady=10)
    date_joined = tk.Entry(animation_window, width=30)
    date_joined.grid(row=6, column=1, padx=10, pady=10)

    label_notable_works = tk.Label(animation_window, text="Notable Works:", font=times_font,bg="lemonchiffon1")
    label_notable_works.grid(row=7, column=0, padx=10, pady=10)
    notable_works = tk.Entry(animation_window, width=30)
    notable_works.grid(row=7, column=1, padx=10, pady=10)

    button_insert_staff_animation = tk.Button(animation_window, text="Add Staff Animation", font=times_font,bg="lightgoldenrod1", command=insert_staff_animation)
    button_insert_staff_animation.grid(row=8, column=1, padx=10, pady=10)


def addStaffProduction():
    production_window = tk.Toplevel(root)
    production_window.title("Add Staff Production")
    production_window.geometry("400x400")
    production_window.configure(bg="lemonchiffon1")
    times_font = Font(family="Times", size=12)

    def insert_staff_production():
        SID = staff_id.get()
        Fname = first_name.get()
        Lname = last_name.get()
        S_job = job_title.get()
        De_DID = department_number.get()
        responisibility = responsibility.get()
        specific_roles = specific_roles_entry.get()  

        # Insert the staff member into the database
        sql_insert_staff = "INSERT INTO stuffmembers VALUES (%s, %s, %s, %s, %s)"
        values_staff = (SID, Fname, Lname, S_job, De_DID)

        # Insert the production staff into the database
        sql_insert_production = "INSERT INTO production_helpers VALUES (%s, %s, %s)"
        values_production = (SID, responisibility, specific_roles)

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(sql_insert_staff, values_staff)
            cursor.execute(sql_insert_production, values_production)
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Staff production added successfully!")
            production_window.destroy()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add staff production: {str(error)}")

    label_staff_id = tk.Label(production_window, text="Staff Member ID:", font=times_font,bg="lemonchiffon1")
    label_staff_id.grid(row=0, column=0, padx=10, pady=10)
    staff_id = tk.Entry(production_window, width=30)
    staff_id.grid(row=0, column=1, padx=10, pady=10)

    label_first_name = tk.Label(production_window, text="First Name:", font=times_font,bg="lemonchiffon1")
    label_first_name.grid(row=1, column=0, padx=10, pady=10)
    first_name = tk.Entry(production_window, width=30)
    first_name.grid(row=1, column=1, padx=10, pady=10)

    label_last_name = tk.Label(production_window, text="Last Name:", font=times_font,bg="lemonchiffon1")
    label_last_name.grid(row=2, column=0, padx=10, pady=10)
    last_name = tk.Entry(production_window, width=30)
    last_name.grid(row=2, column=1, padx=10, pady=10)

    label_job_title = tk.Label(production_window, text="Job Title:", font=times_font,bg="lemonchiffon1")
    label_job_title.grid(row=3, column=0, padx=10, pady=10)
    job_title = tk.Entry(production_window, width=30)
    job_title.grid(row=3, column=1, padx=10, pady=10)

    label_department_number = tk.Label(production_window, text="Department Number:", font=times_font,bg="lemonchiffon1")
    label_department_number.grid(row=4, column=0, padx=10, pady=10)
    department_number = tk.Entry(production_window, width=30)
    department_number.grid(row=4, column=1, padx=10, pady=10)

    label_responsibility = tk.Label(production_window, text="Responsibility:", font=times_font,bg="lemonchiffon1")
    label_responsibility.grid(row=5, column=0, padx=10, pady=10)
    responsibility = tk.Entry(production_window, width=30)
    responsibility.grid(row=5, column=1, padx=10, pady=10)

    label_specific_roles = tk.Label(production_window, text="Specific Roles:", font=times_font,bg="lemonchiffon1")
    label_specific_roles.grid(row=6, column=0, padx=10, pady=10)
    specific_roles_entry = tk.Entry(production_window, width=30)  # Updated variable name
    specific_roles_entry.grid(row=6, column=1, padx=10, pady=10)

    button_insert_staff_production = tk.Button(production_window, text="Add Staff Production", font=times_font,bg="lightgoldenrod1", command=insert_staff_production)
    button_insert_staff_production.grid(row=7, column=1, padx=10, pady=10)


def addEpisode():
    episode_window = tk.Toplevel(root)
    episode_window.title("Add Episode")
    episode_window.geometry("400x300")
    episode_window.configure(bg="lemonchiffon1")
    times_font = Font(family="Times", size=12)

    def insert_episode():
        Acode = project_code.get()
        ESummery = episode_summary.get()
        Etitle = episode_title.get()
        AirDate = episode_air_date.get()
        Enumber = episode_number.get()

        sql_insert = "INSERT INTO episodes VALUES (%s, %s, %s, %s, %s)"
        values = (Acode, ESummery, Etitle, AirDate, Enumber)

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(sql_insert, values)
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Episode added successfully!")
            episode_window.destroy()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add episode: {str(error)}")

    label_episode_number = tk.Label(episode_window, text="Episode Number:", font=times_font,bg="lemonchiffon1")
    label_episode_number.grid(row=0, column=0, padx=10, pady=10)
    episode_number = tk.Entry(episode_window, width=30)
    episode_number.grid(row=0, column=1, padx=10, pady=10)

    label_episode_title = tk.Label(episode_window, text="Episode Title:", font=times_font,bg="lemonchiffon1")
    label_episode_title.grid(row=1, column=0, padx=10, pady=10)
    episode_title = tk.Entry(episode_window, width=30)
    episode_title.grid(row=1, column=1, padx=10, pady=10)

    label_episode_summary = tk.Label(episode_window, text="Episode Summary:", font=times_font,bg="lemonchiffon1")
    label_episode_summary.grid(row=2, column=0, padx=10, pady=10)
    episode_summary = tk.Entry(episode_window, width=30)
    episode_summary.grid(row=2, column=1, padx=10, pady=10)

    label_episode_air_date = tk.Label(episode_window, text="Episode Air Date:", font=times_font,bg="lemonchiffon1")
    label_episode_air_date.grid(row=3, column=0, padx=10, pady=10)
    episode_air_date = tk.Entry(episode_window, width=30)
    episode_air_date.grid(row=3, column=1, padx=10, pady=10)

    label_project_code = tk.Label(episode_window, text="Project Code:", font=times_font,bg="lemonchiffon1")
    label_project_code.grid(row=4, column=0, padx=10, pady=10)
    project_code = tk.Entry(episode_window, width=30)
    project_code.grid(row=4, column=1, padx=10, pady=10)

    button_insert_episode = tk.Button(episode_window, text="Add Episode", font=times_font,bg="lightgoldenrod1", command=insert_episode)
    button_insert_episode.grid(row=5, column=1, padx=10, pady=10)



def addTask():
    task_window = tk.Toplevel(root)
    task_window.title("Add Task")
    task_window.geometry("400x400")
    task_window.configure(bg="lemonchiffon1")
    times_font = Font(family="Times", size=12)

    def insert_task():
        TID = task_id.get()
        Title = task_title.get()
        Task_desc = task_description.get()
        s_date = task_start_date.get()
        e_date = task_end_date.get()
        Enumber = episode_number.get()

        sql_insert = "INSERT INTO atasks VALUES (%s, %s, %s, %s, %s, %s)"
        values = (Title, s_date, e_date, Task_desc, TID, Enumber)

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(sql_insert, values)
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Task added successfully!")
            task_window.destroy()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add task: {str(error)}")

    label_task_id = tk.Label(task_window, text="Task ID:", font=times_font,bg="lemonchiffon1")
    label_task_id.grid(row=0, column=0, padx=10, pady=10)
    task_id = tk.Entry(task_window, width=30)
    task_id.grid(row=0, column=1, padx=10, pady=10)

    label_task_title = tk.Label(task_window, text="Task Title:", font=times_font,bg="lemonchiffon1")
    label_task_title.grid(row=1, column=0, padx=10, pady=10)
    task_title = tk.Entry(task_window, width=30)
    task_title.grid(row=1, column=1, padx=10, pady=10)

    label_task_description = tk.Label(task_window, text="Task Description:", font=times_font,bg="lemonchiffon1")
    label_task_description.grid(row=2, column=0, padx=10, pady=10)
    task_description = tk.Entry(task_window, width=30)
    task_description.grid(row=2, column=1, padx=10, pady=10)

    label_task_start_date = tk.Label(task_window, text="Task Start Date:", font=times_font,bg="lemonchiffon1")
    label_task_start_date.grid(row=3, column=0, padx=10, pady=10)
    task_start_date = tk.Entry(task_window, width=30)
    task_start_date.grid(row=3, column=1, padx=10, pady=10)

    label_task_end_date = tk.Label(task_window, text="Task End Date:", font=times_font,bg="lemonchiffon1")
    label_task_end_date.grid(row=4, column=0, padx=10, pady=10)
    task_end_date = tk.Entry(task_window, width=30)
    task_end_date.grid(row=4, column=1, padx=10, pady=10)

    label_episode_number = tk.Label(task_window, text="Episode Number:", font=times_font,bg="lemonchiffon1")
    label_episode_number.grid(row=5, column=0, padx=10, pady=10)
    episode_number = tk.Entry(task_window, width=30)
    episode_number.grid(row=5, column=1, padx=10, pady=10)

    button_insert_task = tk.Button(task_window, text="Add Task", font=times_font,bg="lightgoldenrod1", command=insert_task)
    button_insert_task.grid(row=6, column=1, padx=10, pady=10)



def addContract():
    contract_window = tk.Toplevel(root)
    contract_window.title("Add Contract")
    contract_window.geometry("400x300")
    contract_window.configure(bg="lemonchiffon1")
    times_font = Font(family="Times", size=12)

    def insert_contract():
        CID = contract_id.get()
        Sdate = contract_start_date.get()
        Edate = contract_end_date.get()
        payment = contract_payment_info.get()

        sql_insert = "INSERT INTO contract VALUES (%s, %s, %s, %s)"
        values = (Sdate, Edate, payment, CID)

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(sql_insert, values)
            connection.commit()
            cursor.close()
            connection.close()
            messagebox.showinfo("Success", "Contract added successfully!")
            contract_window.destroy()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add contract: {str(error)}")

    label_contract_id = tk.Label(contract_window, text="Contract ID:", font=times_font,bg="lemonchiffon1")
    label_contract_id.grid(row=0, column=0, padx=10, pady=10)
    contract_id = tk.Entry(contract_window, width=30)
    contract_id.grid(row=0, column=1, padx=10, pady=10)

    label_contract_start_date = tk.Label(contract_window, text="Contract Start Date:", font=times_font,bg="lemonchiffon1")
    label_contract_start_date.grid(row=1, column=0, padx=10, pady=10)
    contract_start_date = tk.Entry(contract_window, width=30)
    contract_start_date.grid(row=1, column=1, padx=10, pady=10)

    label_contract_end_date = tk.Label(contract_window, text="Contract End Date:", font=times_font,bg="lemonchiffon1")
    label_contract_end_date.grid(row=2, column=0, padx=10, pady=10)
    contract_end_date = tk.Entry(contract_window, width=30)
    contract_end_date.grid(row=2, column=1, padx=10, pady=10)

    label_contract_payment_info = tk.Label(contract_window, text="Contract Payment Info:", font=times_font,bg="lemonchiffon1")
    label_contract_payment_info.grid(row=3, column=0, padx=10, pady=10)
    contract_payment_info = tk.Entry(contract_window, width=30)
    contract_payment_info.grid(row=3, column=1, padx=10, pady=10)

    button_insert_contract = tk.Button(contract_window, text="Add Contract", font=times_font,bg="lightgoldenrod1", command=insert_contract)
    button_insert_contract.grid(row=4, column=1, padx=10, pady=10)



def addViewers():
    viewers_window = tk.Toplevel(root)
    viewers_window.title("Add Viewers")
    viewers_window.geometry("400x200")
    viewers_window.configure(bg="lemonchiffon1")
    times_font = Font(family="Times", size=12)

    def insert_viewer():
        VID = viewer_id.get()
        rate = viewer_rate.get()

        sql_insert = "INSERT INTO viewers VALUES (%s, %s)"
        values = (VID, rate)

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute(sql_insert, values)
            connection.commit()
            cursor.close()
            connection.close()


            messagebox.showinfo("Success", "Viewers added successfully!")
            viewers_window.destroy()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add viewers: {str(error)}")

    label_viewer_id = tk.Label(viewers_window, text="Viewer ID:", font=times_font,bg="lemonchiffon1")
    label_viewer_id.grid(row=0, column=0, padx=10, pady=10)
    viewer_id = tk.Entry(viewers_window, width=30)
    viewer_id.grid(row=0, column=1, padx=10, pady=10)

    label_viewer_rate = tk.Label(viewers_window, text="Viewer Rate:", font=times_font,bg="lemonchiffon1")
    label_viewer_rate.grid(row=1, column=0, padx=10, pady=10)
    viewer_rate = tk.Entry(viewers_window, width=30)
    viewer_rate.grid(row=1, column=1, padx=10, pady=10)

    button_insert_viewer = tk.Button(viewers_window, text="Add Viewers", font=times_font,bg="lightgoldenrod1", command=insert_viewer)
    button_insert_viewer.grid(row=2, column=1, padx=10, pady=10)



def handle_table_selection(event):
    selected_table = table_combobox.get()
    if selected_table == "Department":
        add_department()
    elif selected_table == "Anime Project":
        add_anime_projects()
    elif selected_table == "Stuff members":
        addStaffmember()
    elif selected_table == "Voice actor":
        addStaffVoiceActor()
    elif selected_table == "Staff Animation":
        addStaffAnimation()
    elif selected_table == "Production helpers":
        addStaffProduction()
    elif selected_table == "Episode":
        addEpisode()
    elif selected_table == "Tasks":
        addTask()
    elif selected_table == "Contract":
        addContract()
    elif selected_table == "Viewers":
        addViewers()

    
root = tk.Tk()
root.title("Insert data")
root.geometry("900x450")
times_font = Font(family="Times", size=12)
root.configure(bg="lightgoldenrod1")

style = ttk.Style()

table_label = tk.Label(root, text="Select Table:", font=("Times", 20, "bold") ,bg="lightgoldenrod1")
table_label.pack(anchor="center", side="top")
table_label.configure(highlightbackground="red", highlightcolor="red")

table_combobox = ttk.Combobox(root, values=["Department", "Anime Project", "Stuff members", "Voice actor", "Staff Animation", "Production helpers", "Episode", "Tasks", "Contract", "Viewers"])
table_combobox.pack(anchor="center", side="top")
table_combobox.bind("<<ComboboxSelected>>", handle_table_selection)


root.mainloop()