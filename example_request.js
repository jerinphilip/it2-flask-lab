console.log($.ajax({
        url: 'http://127.0.0.1:5000/addUser',
        data: "username=" + 'Man' + "&email=" + 'abc@xyz.com',
        type: 'POST'
    }))
