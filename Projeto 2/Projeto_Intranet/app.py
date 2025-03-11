from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Dados fictícios que serão exibidos no dashboard
    user_data = {
        'followers': 592000,
        'following': 3500,
        'comments': 2900,
        'likes': 9500,
        'reach': 1.05e6,
        'new_followers': 2700,
        'profile_visits': 22100,
        'link_clicks': 1700,
        'email_button': 592,
        'gender_breakdown': {'female': 61, 'male': 31, 'other': 8},
        'age_groups': {
            '18-24': 35,
            '25-34': 40,
            '35-44': 15,
            '45-54': 10,
        }
    }
    return render_template('dashboard.html', user_data=user_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)