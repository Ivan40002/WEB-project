from flask import Flask, render_template, request, redirect
import smtplib

app = Flask(__name__)
correct_answer = ['1', '2', '2', '3', '3', '1', '2']


def check_task(answers):
    global correct_answer
    counter = 0
    for i in range(len(answers)):
        if correct_answer[i] == answers[i]:
            counter += 1
    return counter


@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        return redirect(f'/test')
    else:
        return render_template('main.html')


@app.route('/test', methods=['POST', 'GET'])
def test():
    answer = []
    if request.method == 'POST':
        question_1 = request.form['question_1']
        answer.append(question_1)
        question_2 = request.form['question_2']
        answer.append(question_2)
        question_3 = request.form['question_3']
        answer.append(question_3)
        question_4 = request.form['question_4']
        answer.append(question_4)
        question_5 = request.form['question_5']
        answer.append(question_5)
        question_6 = request.form['question_6']
        answer.append(question_6)
        question_7 = request.form['question_7']
        answer.append(question_7)
        email = request.form['email']
        result = check_task(answer)
        if email != '':
            if result == 0:
                msg = f'Your result is {result} from 7! do not worry you will definitely learn python'
            elif 1 <= result <= 3:
                msg = f'Your result is {result} from 7! This is quite a good result. The main thing is to continue further and you will definitely succeed.'
            elif 4 <= result <= 6:
                msg = f'Your result is {result} from 7! This is a very good result. You are missing quite a bit of Python knowledge. We hope that you will be able to get the missing knowledge'
            elif result == 7:
                msg = f'Your result is {result} from 7! Congratulations on your good result. You have an impeccable command of Python'
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.starttls()
            smtpObj.login('pythontests2021@gmail.com', 'yGdmdwx3256')
            smtpObj.sendmail("pythontests2021@gmail.com", email, msg)
            smtpObj.quit()
        return redirect(f'/result/{result}')
    else:
        return render_template('testing.html')


@app.route('/result/<int:result>', methods=['POST', 'GET'])
def result_page(result):
    param = {}
    param['result'] = result
    return render_template('result.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
