export const getSuggests = async () => {
    const uri = "/api/question/suggests";
    console.log("uri: ", uri);

    const response = await fetch(uri);
    console.log("response: ", response);
    if (!response.ok) {
        throw new Error("Ошибка загрузки вопросов");
    }

    try {
        const data = await response.json();
        console.log("data: ", data);
        return data.suggests;
    } catch (err) {
        throw new Error("Ошибка форматирования");
    }
};

export const getSuggest = async (uuid) => {
    const uri = "/api/question/suggest?uuid=" + uuid;
    console.log("uri: ", uri);

    const response = await fetch(uri);
    console.log("response: ", response);
    if (!response.ok) {
        throw new Error("Ошибка загрузки вопросов");
    }

    try {
        const data = await response.json();
        console.log("data: ", data);
        return data.suggest;
    } catch (err) {
        throw new Error("Ошибка форматирования");
    }
}