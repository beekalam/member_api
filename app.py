from flask import Flask

app = Flask(__name__)


@app.route('/member', methods=['GET'])
def get_members():
    return 'Hello World!'


@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    return 'member by id'


@app.route('/member', methods=['POST'])
def add_member():
    return 'this adds a member'


@app.route('/member/<int:member_id>', methods=['PUT', 'PATCH'])
def edit_member(member_id):
    return 'this edits a member'


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    return 'this deletes a member'


if __name__ == '__main__':
    app.run(debug=True)
