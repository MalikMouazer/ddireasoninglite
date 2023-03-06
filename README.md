
# How it works ?
It suffices to execute the file "main.py". Two windows will open in the browser corresponding to two tables.these tables summarize and visualize the interactions between several substances.

 - The first one summarizes the interactions by effect. This allows you to see all the interactions that contribute to the modulation of the same effect.
 - The second one summarizes the interactions by substance. This makes it possible to see if and how the bioavailability is modified to take it into account in the dosage adjustment or the possible PD interactions in which the substance will be involved.

You can modify the list of substances to be considered in this demonstration. To do this, you must manually modify the list of substances in the main.py file in the **"drug_test"** variable.

# Database structure :

The database used in this work is in the form of a CSV file "db_ml_interaction_model_mie23.csv".

This database is in a **denomalized format.**

The CSV file contains *6 columns*

*Column 1:* Substance 1 of the interaction
*Column 2:* Substance 2 of the interaction
*Column 3:* The action of the interaction (Increase or decrease of the property). This variable has 2 modalities: ['increase', 'decrease']
*column 4:* The direction of the interaction. Is it "Substance 1" which acts on "Substance 2", the reverse or the addition of the effects of the two substances. It is a question of determining the "victim drug" and the "perpetrator drug". This variable has 3 modalities: ['1/2', '2/1', '1+2']


Name of the fields
The modalities that are pk and those that are pD 
