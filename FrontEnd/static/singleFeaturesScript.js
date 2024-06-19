function goToHome() {
    window.location.href = '/'
}

function submitFormModel(event) {
    event.preventDefault();
    const neighborhood = document.getElementById('neighborhood').value;
    const block = document.getElementById('block').value;
    const lot = document.getElementById('lot').value;
    const url = `/house/model/${neighborhood}/${block}/${lot}`;
    window.location.href = url;
}

function submitFormElevation(event) {
    event.preventDefault();
    const neighborhood = document.getElementById('neighborhood').value;
    const block = document.getElementById('block').value;
    const lot = document.getElementById('lot').value;
    const url = `/house/elevation/${neighborhood}/${block}/${lot}`;
    window.location.href = url;
}

function submitFormColour(event) {
    event.preventDefault();
    const neighborhood = document.getElementById('neighborhood').value;
    const block = document.getElementById('block').value;
    const lot = document.getElementById('lot').value;
    const url = `/house/colour/${neighborhood}/${block}/${lot}`;
    window.location.href = url;
}