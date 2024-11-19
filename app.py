# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/run_script', methods=['POST'])
# def run_script():
#     if request.method == 'POST':
#         # Your Python code or function call here
#         print("Python script is running!")
#         # You can call a function here if you have one
#         # your_function()
#         return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# import subprocess


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/run_script', methods=['POST'])
# def run_script():
#     if request.method == 'POST':
#         # Execute the Python script
#         subprocess.run(["python", "geneticAlgo.py"])  # Replace 'script.py' with your script file name
#         # return redirect(url_for('index'))
#     return render_template('timetable.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# 

# from flask import Flask, render_template, request, redirect, url_for, jsonify
# import subprocess
# import mysql.connector

# app = Flask(__name__)

# # Database connection details
# db_config = {
#     'user': 'root',
#     'password': 'rootroot',
#     'host': 'localhost',
#     'database': 'capstone1',
# }

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/add_faculty', methods=['POST'])
# def add_faculty():
#     if request.method == 'POST':
#         faculty_name = request.form['faculty_name']
#         visiting = request.form['visiting']
#         faculty_id = request.form['faculty_id']

#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()

#             # Insert data into the table
#             sql = "INSERT INTO mytable2(Faculty_Name,Visiting,Faculty_id) VALUES (%s, %s, %s)"
#             cursor.execute(sql, (faculty_name, visiting, faculty_id))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})

# @app.route('/run_script', methods=['POST'])
# def run_script():
#     if request.method == 'POST':
#         # Get input values from the form
#         input1 = request.form['input1'] 
#         input2 = request.form['input2']
#         input3 = request.form['input3']
#         input4 = request.form['input4']

#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()

#             # Insert data into the table
#             sql = "INSERT INTO mytable2(ID,Faculty_Name,Visiting,Faculty_id) VALUES (%s, %s, %s, %s)"
#             cursor.execute(sql, (input1, input2, input3, input4))

#             db.commit()

#             # Run the genetic algorithm script
#             # ... (You can include any additional logic here if needed)
#             subprocess.run(["python", "geneticAlgo.py"]) 

#             return render_template('timetable.html', message="Data inserted successfully! Script executed.")

#         except mysql.connector.Error as error:
#             return render_template('timetable.html', error=f"Failed to insert data: {error}")
#         except subprocess.CalledProcessError as e:
#             return render_template('timetable.html', error=f"An error occurred while running the script: {e}")
#         except Exception as e:
#             return render_template('timetable.html', error=f"An error occurred: {e}")
#         finally:
#             cursor.close()
#             db.close()

#     return render_template('timetable.html')

# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, url_for, jsonify
# import subprocess
# import mysql.connector


# option_list = []

# app = Flask(__name__)

# # Database connection details
# db_config = {
#     'user': 'root',
#     'password': 'rootroot',
#     'host': 'localhost',
#     'database': 'capstone2',  # Use "Gemini" for the database name
# }





# @app.route('/')
# def index():
#     return render_template('index1.html')


# @app.route('/add_C1', methods=['POST'])
# def add_C1():
#     if request.method == 'POST':
        
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '1'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        
            
            
        


# @app.route('/add_C2', methods=['POST'])
# def add_C2():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '2'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        

# @app.route('/add_C3', methods=['POST'])
# def add_C3():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '3'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        


# @app.route('/add_C4', methods=['POST'])
# def add_C4():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '4'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        


# @app.route('/add_C5', methods=['POST'])
# def add_C5():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '5'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        


# @app.route('/add_C6', methods=['POST'])
# def add_C6():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '6'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        


# @app.route('/add_C7', methods=['POST'])
# def add_C7():
#     if request.method == 'POST':
#        try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '8'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#        except mysql.connector.Error as error:
           
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        


# @app.route('/add_C8', methods=['POST'])
# def add_C8():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '9'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        


# @app.route('/add_faculty', methods=['POST'])
# def add_faculty():
#     if request.method == 'POST':
#         id = request.form['id']
#         faculty_name = request.form['faculty_name']
#         visiting = request.form['visiting']
#         faculty_id = request.form['faculty_id']

#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()

#             # Insert data into the table
#             sql = "INSERT INTO mytable2(ID,Faculty_Name,Visiting,Faculty_id) VALUES (%s, %s, %s, %s)"
#             cursor.execute(sql, (id, faculty_name, visiting, faculty_id))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        

# @app.route('/add_Course', methods=['POST'])
# def add_Course():
#     if request.method == 'POST':
#         id = request.form['id1']
#         course_name = request.form['coursename']
#         course_code = request.form['coursecode']
#         sem = request.form['sem']
#         fac_id = request.form['facultyid']
#         nocw = request.form['nocw']
#         type = request.form['type']

#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()

#             # Insert data into the table
#             sql = "INSERT INTO mytable(Course_ID,Course_Name,Course_Code,Semester,Faculty_id,NOCW,Type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#             cursor.execute(sql, (id,course_name,course_code,sem,fac_id,nocw,type))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        
# @app.route('/run_script', methods=['POST'])
# def run_script():
#     if request.method == 'POST':
#         try:
#             # Render the new HTML page when the form is submitted
#             return render_template('index2.html')  # Load new content

#         except Exception as e:
#             # Handle any exceptions and render an error message
#             return f"An unexpected error occurred: {str(e)}"
        
# @app.route('/run_script1', methods=['POST'])
# def run_script1():
#     if request.method == 'POST':
#         try:
#             # Render the new HTML page when the form is submitted
#             return render_template('index3.html')  # Load new content

#         except Exception as e:
#             # Handle any exceptions and render an error message
#             return f"An unexpected error occurred: {str(e)}"
            


# @app.route('/run_script3', methods=['POST'])
# def run_script3():
#     if request.method == 'POST':
#         try:
#             # Run the genetic algorithm script
#             process = subprocess.run(["python", "geneticAlgo.py"], capture_output=True, text=True)

#             # Handle the output from geneticAlgo.py
#             output = process.stdout  # Capture standard output
#             if output:
#                 return render_template('timetable.html', output=output)
#             else:
#                 return render_template('timetable.html', error="Script completed without output.")

#         except subprocess.CalledProcessError as e:
#             return render_template('timetable.html', error=f"An error occurred while running the script: {e}")
#         except Exception as e:
#             return render_template('timetable.html', error=f"An error occurred: {e}")
        
        
# @app.route('/delete-num-column', methods=['POST'])
# def delete_num_column():
#     try:
#         # Connect to the database
#         db = mysql.connector.connect(**db_config)
#         cursor = db.cursor()

#         # Delete the num column from the database table
#         sql = "DELETE FROM mytable3 WHERE num IS NOT NULL"
#         cursor.execute(sql)
#         db.commit()

#         return jsonify({'status': 'success', 'message': 'Column num deleted successfully'})

#     except mysql.connector.Error as error:
#         app.logger.error(f"Failed to delete num column: {error}")
#         return jsonify({'status': 'error', 'message': f"Failed to delete num column: {error}"})

#     finally:
#         cursor.close()
#         db.close()


        
# @app.route('/delete', methods=['POST'])
# def delete():
#     try:
#         # Connect to the database
#         db = mysql.connector.connect(**db_config)
#         cursor = db.cursor()

#         # Delete the num column from the database table
#         sql = "DELETE FROM mytable3 WHERE num IS NOT NULL"
#         cursor.execute(sql)
#         db.commit()

#         return jsonify({'status': 'success', 'message': 'Column num deleted successfully'})

#     except mysql.connector.Error as error:
#         app.logger.error(f"Failed to delete num column: {error}")
#         return jsonify({'status': 'error', 'message': f"Failed to delete num column: {error}"})

#     finally:
#         cursor.close()
#         db.close()         
        


# if __name__ == '__main__':
#     app.run(debug=True)
# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/run_script', methods=['POST'])
# def run_script():
#     if request.method == 'POST':
#         # Your Python code or function call here
#         print("Python script is running!")
#         # You can call a function here if you have one
#         # your_function()
#         return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for
# import subprocess


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/run_script', methods=['POST'])
# def run_script():
#     if request.method == 'POST':
#         # Execute the Python script
#         subprocess.run(["python", "geneticAlgo.py"])  # Replace 'script.py' with your script file name
#         # return redirect(url_for('index'))
#     return render_template('timetable.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# 

# from flask import Flask, render_template, request, redirect, url_for, jsonify
# import subprocess
# import mysql.connector

# app = Flask(__name__)

# # Database connection details
# db_config = {
#     'user': 'root',
#     'password': 'rootroot',
#     'host': 'localhost',
#     'database': 'capstone1',
# }

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/add_faculty', methods=['POST'])
# def add_faculty():
#     if request.method == 'POST':
#         faculty_name = request.form['faculty_name']
#         visiting = request.form['visiting']
#         faculty_id = request.form['faculty_id']

#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()

#             # Insert data into the table
#             sql = "INSERT INTO mytable2(Faculty_Name,Visiting,Faculty_id) VALUES (%s, %s, %s)"
#             cursor.execute(sql, (faculty_name, visiting, faculty_id))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})

# @app.route('/run_script', methods=['POST'])
# def run_script():
#     if request.method == 'POST':
#         # Get input values from the form
#         input1 = request.form['input1'] 
#         input2 = request.form['input2']
#         input3 = request.form['input3']
#         input4 = request.form['input4']

#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()

#             # Insert data into the table
#             sql = "INSERT INTO mytable2(ID,Faculty_Name,Visiting,Faculty_id) VALUES (%s, %s, %s, %s)"
#             cursor.execute(sql, (input1, input2, input3, input4))

#             db.commit()

#             # Run the genetic algorithm script
#             # ... (You can include any additional logic here if needed)
#             subprocess.run(["python", "geneticAlgo.py"]) 

#             return render_template('timetable.html', message="Data inserted successfully! Script executed.")

#         except mysql.connector.Error as error:
#             return render_template('timetable.html', error=f"Failed to insert data: {error}")
#         except subprocess.CalledProcessError as e:
#             return render_template('timetable.html', error=f"An error occurred while running the script: {e}")
#         except Exception as e:
#             return render_template('timetable.html', error=f"An error occurred: {e}")
#         finally:
#             cursor.close()
#             db.close()

#     return render_template('timetable.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, jsonify
import subprocess
import mysql.connector


option_list = []

app = Flask(__name__)

# Database connection details
db_config = {
    'user': 'root',
    'password': 'rootroot',
    'host': 'localhost',
    'database': 'capstone2',  
}





@app.route('/')
def index():
    return render_template('index1.html')


# @app.route('/add_C1', methods=['POST'])
# def add_C1():
#     if request.method == 'POST':
        
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '1'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        
            
            
        


# @app.route('/add_C2', methods=['POST'])
# def add_C2():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '2'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        

# @app.route('/add_C3', methods=['POST'])
# def add_C3():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '3'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        


# @app.route('/add_C4', methods=['POST'])
# def add_C4():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '4'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        


# @app.route('/add_C5', methods=['POST'])
# def add_C5():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '5'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        


# @app.route('/add_C6', methods=['POST'])
# def add_C6():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '6'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        


# @app.route('/add_C7', methods=['POST'])
# def add_C7():
#     if request.method == 'POST':
#        try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '8'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#        except mysql.connector.Error as error:
           
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        


# @app.route('/add_C8', methods=['POST'])
# def add_C8():
#     if request.method == 'POST':
#         try:
#             # Connect to the database
#             db = mysql.connector.connect(**db_config)
#             cursor = db.cursor()
#             id = '9'
#             # Insert data into the table
#             sql = "INSERT INTO mytable3(num) VALUES (%s)"
#             cursor.execute(sql, (id,))

#             db.commit()
#             cursor.close()
#             db.close()

#             return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

#         except mysql.connector.Error as error:
#             return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
@app.route('/add-faculty-id', methods=['POST'])
def add_faculty_id():
    faculty_id = request.json.get('id')
    
    if not faculty_id.isdigit():
        return jsonify({'error': 'Invalid faculty ID'}), 400

    # Append '0' to the faculty ID
    adjusted_id = int(faculty_id + '0')  # Append '0' and convert to integer

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Insert the adjusted ID into the database
        cursor.execute(
            "INSERT INTO faculty_ids (adjusted_id) VALUES (%s) ON DUPLICATE KEY UPDATE adjusted_id = %s",
            (adjusted_id, adjusted_id)
        )
        connection.commit()
        
        return jsonify({'message': f'Adjusted ID {adjusted_id} added successfully'}), 200
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
       
@app.route('/update_constraints', methods=['POST'])
def update_constraints():
    try:
        # Parse the JSON payload from the request
        data = request.get_json()  # This will automatically parse the JSON body
        if not data:
            return jsonify({'status': 'error', 'message': 'No JSON data received.'})

        constraint_id = data.get('constraint_id')
        action = data.get('action')

        if not constraint_id or not action:
            return jsonify({'status': 'error', 'message': 'Invalid data provided.'})

        # Connect to the database
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        # Perform action based on the requested action ('add' or 'delete')
        if action == 'add':
            # Insert the constraint if it doesn't already exist
            sql_insert_constraint = "INSERT IGNORE INTO mytable3 (num) VALUES (%s)"
            cursor.execute(sql_insert_constraint, (constraint_id,))
            db.commit()
            return jsonify({'status': 'success', 'message': 'Constraint added successfully!'})
        
        elif action == 'delete':
            # Delete the constraint
            sql_delete_constraint = "DELETE FROM mytable3 WHERE num = %s"
            cursor.execute(sql_delete_constraint, (constraint_id,))
            db.commit()
            return jsonify({'status': 'success', 'message': 'Constraint deleted successfully!'})
        
        else:
            return jsonify({'status': 'error', 'message': 'Invalid action.'})

    except mysql.connector.Error as error:
        return jsonify({'status': 'error', 'message': f"Failed to process request: {error}"})

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()


@app.route('/add_faculty', methods=['POST'])
def add_faculty():
    if request.method == 'POST':
        id = request.form['id']
        faculty_name = request.form['faculty_name']
        visiting = request.form['visiting']
        faculty_id = request.form['faculty_id']

        try:
            # Connect to the database
            db = mysql.connector.connect(**db_config)
            cursor = db.cursor()

            # Insert data into the table
            sql = "INSERT INTO mytable2(ID,Faculty_Name,Visiting,Faculty_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (id, faculty_name, visiting, faculty_id))

            db.commit()
            cursor.close()
            db.close()

            return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

        except mysql.connector.Error as error:
            return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        

@app.route('/add_Course', methods=['POST'])
def add_Course():
    if request.method == 'POST':
        id = request.form['id1']
        course_name = request.form['coursename']
        course_code = request.form['coursecode']
        sem = request.form['sem']
        fac_id = request.form['facultyid']
        nocw = request.form['nocw']
        type = request.form['type']

        try:
            # Connect to the database
            db = mysql.connector.connect(**db_config)
            cursor = db.cursor()

            # Insert data into the table
            sql = "INSERT INTO mytable(Course_ID,Course_Name,Course_Code,Semester,Faculty_id,NOCW,Type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (id,course_name,course_code,sem,fac_id,nocw,type))

            db.commit()
            cursor.close()
            db.close()

            return jsonify({'status': 'success', 'message': 'Faculty added successfully!'})

        except mysql.connector.Error as error:
            return jsonify({'status': 'error', 'message': f"Failed to insert data: {error}"})
        
@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    # Parse JSON data from the request
    data = request.get_json()
    selected_values = data.get('faculty', [])

    if not selected_values:
        return jsonify({'message': 'No faculty selected!'}), 400

    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert selected values into the database
        for value in selected_values:
            cursor.execute("INSERT INTO mytable4 (teach) VALUES (%s)", (value,))

        # Commit the transaction
        connection.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({'message': 'Database error occurred!'}), 500

    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

    return jsonify({'message': 'Faculty selection saved successfully!'})

@app.route('/add_timeslot', methods=['POST'])
def add_timeslot():
    # Parse the JSON data sent from the frontend
    data = request.get_json()
    selected_timeslot = data.get('timeslot')

    if selected_timeslot is None:
        return jsonify({'message': 'No timeslot selected!'}), 400

    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert the selected timeslot into the database
        cursor.execute("INSERT INTO mytable4 (slot) VALUES (%s)", (selected_timeslot,))

        # Commit the transaction
        connection.commit()

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return jsonify({'message': 'Database error occurred!'}), 500

    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()

    return jsonify({'message': 'Timeslot saved successfully!'})

      
@app.route('/run_script', methods=['POST'])
def run_script():
    if request.method == 'POST':
        try:
            # Render the new HTML page when the form is submitted
            return render_template('index2.html')  # Load new content

        except Exception as e:
            # Handle any exceptions and render an error message
            return f"An unexpected error occurred: {str(e)}"
        
@app.route('/run_script1', methods=['POST'])
def run_script1():
    if request.method == 'POST':
        try:
            # Render the new HTML page when the form is submitted
            return render_template('index3.html')  # Load new content

        except Exception as e:
            # Handle any exceptions and render an error message
            return f"An unexpected error occurred: {str(e)}"
            


@app.route('/run_script3', methods=['POST'])
def run_script3():
    if request.method == 'POST':
        try:
            # Run the genetic algorithm script
            process = subprocess.run(["python", "geneticAlgo.py"], capture_output=True, text=True)

            # Handle the output from geneticAlgo.py
            output = process.stdout  # Capture standard output
            if output:
                return render_template('timetable.html', output=output)
            else:
                return render_template('timetable.html', error="Script completed without output.")

        except subprocess.CalledProcessError as e:
            return render_template('timetable.html', error=f"An error occurred while running the script: {e}")
        except Exception as e:
            return render_template('timetable.html', error=f"An error occurred: {e}")
        
        
@app.route('/delete-num-column', methods=['POST'])
def delete_num_column():
    try:
        # Connect to the database
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        # Delete the num column from the database table
        sql = "DELETE FROM mytable3 WHERE num IS NOT NULL"
        cursor.execute(sql)
        db.commit()

        return jsonify({'status': 'success', 'message': 'Column num deleted successfully'})

    except mysql.connector.Error as error:
        app.logger.error(f"Failed to delete num column: {error}")
        return jsonify({'status': 'error', 'message': f"Failed to delete num column: {error}"})

    finally:
        cursor.close()
        db.close()
        
@app.route('/delete', methods=['POST'])
def delete():
    try:
        # Connect to the database
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        # Delete the num column from the database table
        sql = "DELETE FROM mytable3 WHERE num IS NOT NULL"
        cursor.execute(sql)
        db.commit()

        return jsonify({'status': 'success', 'message': 'Column num deleted successfully'})

    except mysql.connector.Error as error:
        app.logger.error(f"Failed to delete num column: {error}")
        return jsonify({'status': 'error', 'message': f"Failed to delete num column: {error}"})

    finally:
        cursor.close()
        db.close()         
        


if __name__ == '__main__':
    app.run(debug=True)
