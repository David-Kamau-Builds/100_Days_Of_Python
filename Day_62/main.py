from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from forms import CafeForm
from config import SECRET_KEY, CSV_FILE_PATH
import csv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap5(app)


def cafe_exists(cafe_name):
    """Check if cafe already exists in CSV"""
    try:
        with open(CSV_FILE_PATH, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip header
            for row in csv_reader:
                if row and row[0].lower() == cafe_name.lower():
                    return True
    except FileNotFoundError:
        pass
    return False


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # Check for duplicate cafe
        if cafe_exists(form.cafe.data):
            flash('A cafe with this name already exists!', 'error')
            return render_template('add.html', form=form)
        
        try:
            # Create CSV file with headers if it doesn't exist
            if not CSV_FILE_PATH.exists():
                with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(['Cafe Name', 'Location', 'Open', 'Close', 'Coffee', 'Wifi', 'Power'])
            
            # Append new cafe data using csv.writer
            with open(CSV_FILE_PATH, 'a', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([
                    form.cafe.data,
                    form.location.data,
                    form.open_time.data,
                    form.close_time.data,
                    form.coffee_rating.data,
                    form.wifi_strength.data,
                    form.power_socket.data
                ])
            
            flash('Cafe added successfully!', 'success')
            return redirect(url_for('cafes'))
            
        except PermissionError:
            flash('Permission denied: Cannot write to file.', 'error')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
    
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    try:
        with open(CSV_FILE_PATH, 'r', newline='', encoding='utf-8') as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            list_of_rows = list(csv_data)
        return render_template('cafes.html', cafes=list_of_rows)
    except FileNotFoundError:
        flash('No cafe data found. Add some cafes first!', 'error')
        return redirect(url_for('home'))
    except Exception as e:
        flash(f'Error reading cafe data: {str(e)}', 'error')
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
