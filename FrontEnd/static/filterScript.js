document.addEventListener("DOMContentLoaded", function() {
    modelOptions = {'44 ft' : ['Armstrong','Bishop','Borgeua','Cline','Maclaren','Ptarmigan','Rutherford','Smythe','Bishop 2.0','Aberdeen','Rundle','Bluebell'],
        '36 ft' : ['Cypress','Fairview','Fullerton','Monarch','Whistler','Yamnuska','Norquay'],
        '24 ft' : ['Waputik','Palliser','Sundance','Finch','Cardinal','Starling']};
    const elevations = ["CR","CL","PR"];
    const colourOptions = {'CL' : ['CL - 1.1', 'CL - 2.1', 'CL - 3.1', 'CL - 4.1','CL - 5.1','CL - 6.1','CL - 7.1','CL - 8.1','CL - 9.1','CL - 10.1'],
        'CR' : ['CR - 1.1', 'CR - 2.1', 'CR - 3.1', 'CR - 4.1','CR - 5.1','CR - 6.1','CR - 7.1','CR - 8.1','CR - 9.1','CR - 10.1'],
        'PR' : ['PR - 1.1', 'PR - 2.1', 'PR - 3.1', 'PR - 4.1','PR - 5.1','PR - 6.1','PR - 7.1','PR - 8.1','PR - 9.1','PR - 10.1']};

    function populateDropdown(id, options) {
        const select = document.getElementById(id);
        select.innerHTML = ""; // Clear existing options
        options.forEach(option => {
            const opt = document.createElement('option');
            opt.value = option;
            opt.innerHTML = option;
            select.appendChild(opt);
        });
    }

    function updateModels() {
        const footage = document.getElementById('footage').value;
        populateDropdown('model', modelOptions[footage]);
    }

    function updateColours(){
        const elevation = document.getElementById('elevation').value;
        populateDropdown('colour',colourOptions[elevation])
    }

    document.getElementById('footage').addEventListener('change', updateModels);
    document.getElementById('elevation').addEventListener('change',updateColours);

    populateDropdown('elevation', elevations);
    updateModels();
    updateColours();
});