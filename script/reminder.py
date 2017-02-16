#!/usr/bin/python
# coding: utf-8

import subprocess
import sys

def main():

    #print 'Args:', str(sys.argv)

    args = sys.argv[1].split()
    #print args

    # Command to be run after the needed time
    # Update your API info for this command to work.
    bashCommand = """at #REMINDER_TIME# << EOF
    curl -i --user "admin":"secret" -H "Content-Type: application/json" -X POST -d '{"order":"api-repeat-cmd #MESSAGE#"}' http://localhost:5000/order/
    EOF"""

    # Query pattern:
    # dans {{minutes}} minutes de {{message}}

    # Mispelling on purpose to force right pronounciation and avoid charset issue
    message = "Monsieur, vous mavez demander de vous rappeler de "
    end_message = ""

    # If the reminder is in X minutes
    if args[0] == "dans":
        # args[2] should be minutes or hours
        reminder_time = "now + " + args[1] + " " +args[2]
        # args[3] should be always "de"
        for i in range(4, len(args)):
            message += args[i] + " "
        #print("reminder time: %s" % reminder_time)
        #print("message: %s" % message)

        # Mispelling on purpose to force right pronounciation and avoid charset issue
        end_message = "Rappel programmer dans " + args[1] + " minutes"

    # If the reminder is at a specific time
    elif args[0] == "à":
        # TODO
        print('Le rappelle a heure précise n\'est pas disponible')
    else:
        # TODO
        print('Erreur')

    bashCommand = bashCommand.replace("#MESSAGE#", message).replace("#REMINDER_TIME#", reminder_time)

    p = subprocess.Popen(bashCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # for Kalliopé to read:
    print end_message


if __name__ == "__main__":
    main()
