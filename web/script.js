
async function get_text(){

    query_value = document.getElementById("search").value;

    let all_text = await eel.scraper(query_value)();
    document.getElementById("main_text").textContent = all_text[0];
    document.getElementById("result_title").textContent = all_text[1];
}

$("#submit").click(function(){
    get_text();
})