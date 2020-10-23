// Saving Languages

// console.log("Hello");

// showSaved();

function save_lang(name)
{
    // console.log(name);
    let lang = localStorage.getItem('saved_languages');
    if(lang==null)
    {
        langObj = [];
    }
    else
    {
        langObj = JSON.parse(lang);
    }
    // console.log(langObj);
    let lang_name = document.getElementById(`save_${name}`);
    // console.log(lang_name);
    index = langObj.indexOf(name);
    // console.log("index",index);
    if(index!=-1)
    {
        del = langObj.splice(index,1);
        // console.log("deleted",del);
        lang_name.innerText = "Save";
    }
    else
    {
        langObj.push(name);
        lang_name.innerText = "Saved";
    }
    // console.log("new langobj", langObj);
    localStorage.setItem('saved_languages',JSON.stringify(langObj));
    showSaved();
}

function showSaved()
{
    let lang = localStorage.getItem('saved_languages');
    if(lang==null)
    {
        langObj = [];
    }
    else
    {
        langObj = JSON.parse(lang);
    }
    // console.log(langObj);
    let btns = document.getElementsByClassName('save_button');
    Array.from(btns).forEach(function(element){
        if(langObj.includes(element.name))
        {
            element.innerText = "Saved";
        }
        else
        {
            element.innerText = "Save";
        }
    })
}

// Over

function load_saved()
{
    let btns = document.getElementsByClassName('card-title');
    let lang = localStorage.getItem('saved_languages');
    if(lang==null)
    {
        langObj = [];
    }
    else
    {
        langObj = JSON.parse(lang);
    }
    console.log(Array.from(langObj).length);
    if(Array.from(langObj).length==0)
    {
        document.getElementById('cards').innerHTML = "<div><h3>No Saved Languages</h3></div>";        
    }
    else
    {
        Array.from(btns).forEach(function(element){
            if(!langObj.includes(element.innerText))
            {
                document.getElementById(`${element.innerText}`).style.display = 'none';
            }
        });        
    }
}

function reload_saved(name)
{
    // console.log(name);
    let lang = localStorage.getItem('saved_languages');
    if(lang==null)
    {
        langObj = [];
    }
    else
    {
        langObj = JSON.parse(lang);
    }
    // console.log(langObj);
    let lang_name = document.getElementById(`save_${name}`);
    // console.log(lang_name);
    index = langObj.indexOf(name);
    // console.log("index",index);
    if(index!=-1)
    {
        del = langObj.splice(index,1);
        // console.log("deleted",del);
        lang_name.innerText = "Save";
    }
    else
    {
        langObj.push(name);
        lang_name.innerText = "Saved";
    }
    // console.log("new langobj", langObj);
    localStorage.setItem('saved_languages',JSON.stringify(langObj));
    load_saved();
}