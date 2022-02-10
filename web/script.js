
let div_res = document.createElement('div');
div_res.className = 'result';

let div_wrap =  document.createElement('div');
div_wrap.className = "result_wrap";

let res_title = document.createElement('h3');
res_title.className = 'result_title';

let res_img = document.createElement('img');
res_img.className = 'article_img_hidden';

let main_text = document.createElement('p');
main_text.className = 'main_text';

//div_res.append(div_wrap);
//div_wrap.append(res_title);
//div_wrap.append(res_img);
//div_wrap.append(main_text);

let main_div = document.getElementsByClassName("results")[0];
main_div.append(div_res);



async function get_text(){

    query_value = document.getElementById("search").value;

    let all_text = await eel.scraper(query_value)();
    document.getElementsByClassName("main_text")[0].textContent = all_text[0];
    document.getElementsByClassName("result_title")[0].textContent = all_text[1];
    document.getElementsByClassName("article_img_hidden")[0].src = all_text[2];
    document.getElementsByClassName("article_img_hidden")[0].className = "article_img";
}

$("#submit").click(function(){
    get_text();
})