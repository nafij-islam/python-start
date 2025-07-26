# print("Hello python")
# x=40
# y=30

# sum=x+y

# print(sum)

# if y > x:
#     print("hello world")

# else: print("hello javascrip")


# list=["apple", "banana", "mango"]

# print(list[3:])

# if "apple" in list:
#     print('yes apple is in the list')




from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/show-text', methods=['POST'])
def show_text():
    return "<h2>Hello from Python (Flask)!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
