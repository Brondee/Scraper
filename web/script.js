
async function get_text(){

    let all_text = await eel.txt_reader()();

    document.getElementById("main_text").textContent = all_text;

}

$("#submit").click(function(){
    get_text();
})