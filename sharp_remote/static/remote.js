function remoteKeyPress(keyname) {
	// Map keys to remote buttons...
	key = null;
	switch(keyname) {
		case 'Power':  // FIXME: use POWR here? button doesn't work when TV is Off...
			key = '12';
			break;
		case 'Display':
			key = '13';
			break;
		case 'Power_Source':
			key = '14';
			break;
		// The following are input selection, invalid
		case 'SelTV':
			key = 'errSel';
			break;
		case 'SelSTB':
			key = 'errSel';
			break;
		case 'SelDVD':
			key = 'errSel';
			break;
		case 'SelAudio':
			key = 'errSel';
			break;
		case 'Rev':
			key = '15';
			break;
		case 'Play':
			key = '16';
			break;
		case 'Fwd':
			key = '17';
			break;
		case 'Pause':
			key = '18';
			break;
		case 'Prev':
			key = '19';
			break;
		case 'Stop':
			key = '20';
			break;
		case 'Next':
			key = '21';
			break;
		case 'Rec':
			key = '22';
			break;
		case 'Option':
			key = '23';
			break;
		case 'Sleep':
			key = '24';
			break;
		case 'Audio':
			key = '49';
			break;
		case 'Freeze':
			key = '54';
			break;
		case '1':
			key = '01';
			break;
		case '2':
			key = '02';
			break;
		case '3':
			key = '03';
			break;
		case '4':
			key = '04';
			break;
		case '5':
			key = '05';
			break;
		case '6':
			key = '06';
			break;
		case '7':
			key = '07';
			break;
		case '8':
			key = '08';
			break;
		case '9':
			key = '09';
			break;
		case '.':
			key = '10';
			break;
		case '0':
			key = '00';
			break;
		case 'Ent':
			key = '11';
			break;
		case 'CC':
			key = '27';
			break;
		case 'AVMode':
			key = '28';
			break;
		case 'ViewMode':
			key = '29';
			break;
		case 'Flashback':
			key = '30';
			break;
		case 'Mute':
			key = '31';
			break;
		case 'Vol+':
			key = '33';
			break;
		case 'Vol-':
			key = '32';
			break;
		case 'CH+':
			key = '34';
			break;
		case 'CH-':
			key = '35';
			break;
		case 'Input':
			key = '36';
			break;
		case '3D':
			key = '58';
			break;
		case 'Menu':
			key = '38';
			break;
		case 'SmartCentral':
			key = '39';
			break;
		case 'Left':
			key = '43';
			break;
		case 'Right':
			key = '44';
			break;
		case 'Up':
			key = '41';
			break;
		case 'Down':
			key = '42';
			break;
		case 'Enter':
			key = '40';
			break;
		case 'Exit':
			key = '46';
			break;
		case 'Return':
			key = '45';
			break;
		case 'Netflix':
			key = '59';
			break;
		case 'Favorite':
			key = '47';
			break;
		case 'Fav1':
			key = '55';
			break;
		case 'Fav2':
			key = '56';
			break;
		case 'Fav3':
			key = '57';
			break;
		case 'A':
			key = '50';
			break;
		case 'B':
			key = '51';
			break;
		case 'C':
			key = '52';
			break;
		case 'D':
			key = '53';
			break;
	}
	if (!key) {
		throw 'ERROR: remoteKeyPress: Key ' + keyname + 'missing';
	}

	// TODO: notify user on invalid buttons
	const userAction = async () => {
		const settings = {
			method: 'PUT',
			headers: { Accept: 'application/json' },
		};

		const resp = await fetch('/api/command/RCKY/' + key, settings);
		const res = await resp.json();
		// TODO: notify user
		console.log(res.message);
	}
	userAction();
}
