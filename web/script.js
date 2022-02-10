



async function get_text(){

    query_value = document.getElementById("search").value;

    let python_func = await eel.scraper(query_value)();

    let counter = python_func[3]

    for(let i = 0; i < counter; i++){

        let div_res = document.createElement('div');
        div_res.className = 'result';

        let div_wrap =  document.createElement('div');
        div_wrap.className = "result_wrap";

        let res_title = document.createElement('h3');
        res_title.className = 'result_title';

        let res_img = document.createElement('img');
        res_img.className = 'article_img_hidden';

        let res_text = document.createElement('p');
        res_text.className = 'main_text';

        let main_div = document.getElementsByClassName("results")[0];
        main_div.append(div_res);

        div_res.append(div_wrap);
        div_wrap.append(res_title);
        div_wrap.append(res_img);
        div_wrap.append(res_text);

        let func_title = python_func[0][i];
        let func_img = python_func[1][i];
        let func_text = python_func[2][i];

        res_title.innerText = func_title;
        res_img.src = func_img;
        res_img.className = "article_img";
        res_text.innerText = func_text;
    }
}

$("#submit").click(function(){
    get_text();
})