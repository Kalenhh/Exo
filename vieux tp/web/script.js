function convertir(formulaire)
{
	if (document.formulaire.conv1.checked==true)
	{
		document.formulaire.ms.value=document.formulaire.kmh.value/3.6;
		
	}
	if (document.formulaire.conv2.checked==true)
	{
		document.formulaire.kmh.value=document.formulaire.ms.value*3.6;

	}
}