var updateBtns = document.getElementsByClassName('updatecart')

for(var i=0; i< updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action',action)

        console.log('USER :', user)
        if (user == 'AnonymousUser'){
            console.log('user is not autenticated')
        }else{
            updateUserOrder(productId,action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('user is logged in, sending data ...')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId': productId, 'action':action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log('data:', data)
        location.reload() //to reload the page and see the resultes immediatly
    })
}