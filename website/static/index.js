
function deleteNote(noteId){
    fetch('/delete-node', {
        method: 'POST',
        body: JSON.stringify({noteId: noteId})
    }).then((value) => {
        if(value.status == 200){
            window.location.href = '/';
        }
    })
}