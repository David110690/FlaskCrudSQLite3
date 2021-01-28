const btnDelete = document.querySelectorAll('.btn-delete') 

if(btnDelete){  
    const btnArray = Array.from(btnDelete); 
    btnDelete.forEach((btn) => { 
        btn.addEventListener('click', (e) => { 
            if (!confirm('Desea eliminar?')){ 
                e.preventDefault();
                
            }
        });
    });
}





