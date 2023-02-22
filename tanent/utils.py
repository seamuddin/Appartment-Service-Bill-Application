from tanent.models import Tanent, FlatChangeHistory
from datetime import datetime
from flat.models import Flat

def tanent_data_check_on_change_history():
    tanent = Tanent.objects.all()
    for i in tanent:
        history = FlatChangeHistory.objects.filter(tanent=i,status=0).values()
        if history:
            for j in history:
                if i.date <= datetime.today().date():
                    i_tanent = Tanent.objects.get(id=j.get('tanent_id'))
                    i_tanent.flat = Flat.objects.get(id=j.get('flat_id'))
                    i_tanent.date = j.get('date')
                    i_tanent.end_date = None
                    i_tanent.status = 1
                    i_tanent.save()

                    history_data = FlatChangeHistory.objects.get(id=j.get('id'))
                    history_data.status = 1
                    history_data.save()


