document.getElementById("sendbtn").addEventListener("click", () => {
    const reader = new FileReader();
    const currentLang = document.getElementsByName('mainLanguage')[0].value;
    const file = document.getElementsByName("file")[0].files[0];

    reader.addEventListener("loadend", (data) => {
        let keysCounter = 0;
        let langCounter = 0;
        const fileData = JSON.parse(data.target.result);
        const transleteKeys = Object.keys(fileData);
        const langKeys = Object.keys(fileData[transleteKeys[0]]);

        const intervalNumber = setInterval(async () => {
            while (true) {
                let transleteObj = fileData[transleteKeys[keysCounter]];
                let transleteLang = langKeys[langCounter];
                if (transleteLang !== currentLang || !transleteObj[transleteLang]) {
                    let url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl="
                        + currentLang + "&tl=" + transleteLang + "&dt=t&q=" + transleteObj[currentLang];
                    await fetch(url).then((response) => response.json()).then((translation) => {
                        transleteObj[transleteLang] = translation[0][0][0];
                    });
                    if (++langCounter >= langKeys.length) {
                        langCounter = 0;
                        keysCounter++;
                    }
                    break;
                } else {
                    if (++langCounter >= langKeys.length) {
                        langCounter = 0;
                        keysCounter++;
                        if (keysCounter >= transleteKeys.length) break;
                    }
                }
            }

            if (keysCounter >= transleteKeys.length) {
                clearInterval(intervalNumber);
                //browser.downloads.download(new Blob([JSON.stringify(transleteObj)]))
                const anchor = document.createElement("a");
                anchor.href = URL.createObjectURL(new Blob([JSON.stringify(fileData)]));
                anchor.download = file.name;
                anchor.click();
            };
        }, 1000);


    });
    reader.readAsText(file);
})
