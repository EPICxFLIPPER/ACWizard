function submitForm(event) {
    event.preventDefault();
    const neighborhood = document.getElementById('neighborhood').value;
    const block = document.getElementById('block').value;
    const lot = document.getElementById('lot').value;
    const url = `/house/${neighborhood}/${block}/${lot}`;
    window.location.href = url;
}

function goToSingleFeatures() {
    window.location.href = '/singleFeatures'
}

function goToUpdatePage(neighborhood,block,lot,model,elevation,colour) {
    const url = `/update?neighborhood=${encodeURIComponent(neighborhood)}&block=${encodeURIComponent(block)}&lot=${encodeURIComponent(lot)}&model=${encodeURIComponent(model)}&elevation=${encodeURIComponent(elevation)}&colour=${encodeURIComponent(colour)}`;
    window.location.href = url;
}