# Create your views here.

# --- Django imports ---
from django.http import JsonResponse
from django.views import View

# --- Core/Librerías propias ---
from core.myLib.geometryTools import WkbConversor, GeometryChecks
from core.myLib.baseDjangoView import BaseDjangoView

# --- Tus clases de Base de Datos (Operaciones) ---
from forestal.operations.arbolesDjango import ArbolesDjango
from forestal.operations.caminosDjango import CaminosDjango   
from forestal.operations.parcelasDjango import ParcelasDjango


# ==========================================
# VISTAS DE PRUEBA / BÁSICAS PARA ARBOLES
# ==========================================
class HelloForestal(View):
    def get(self, request):
        return JsonResponse({"ok": True, "message": "Forestal. Hello world", "data": [request.GET.dict()]})
        
    def post(self, request):
        return JsonResponse({"ok": True, "message": "Forestal. Hello world", "data": [request.POST.dict()]})

class ForestalInsert(View):
    def post(self, request):
        d = request.POST.dict()
        db_arboles = ArbolesDjango()
        r = db_arboles.insert(d)
        return JsonResponse(r)

class ForestalDelete(View):
    def post(self, request):
        d = request.POST.dict()
        db_arboles = ArbolesDjango()
        r = db_arboles.delete(d)
        return JsonResponse(r)


# ==========================================
# VISTAS PRINCIPALES (Heredan de BaseDjangoView)
# ==========================================

# --- ARBOLES ---
class ForestalView(BaseDjangoView):
    # GET OPERATIONS
    def selectone(self, id):
        db_arboles = ArbolesDjango()
        r = db_arboles.selectAsDicts({'id': id}) 
        return JsonResponse(r)

    def selectall(self):
        db_arboles = ArbolesDjango()
        # r = db_arboles.selectAll() # Descomenta cuando agregues este método a tu script
        return JsonResponse({"ok": False, "message": "Método selectall no implementado para Arboles aún"})

    # POST OPERATIONS
    def insert(self, request):
        d = request.POST.dict()
        db_arboles = ArbolesDjango()
        r = db_arboles.insert(d)
        return JsonResponse(r)
        
    def update(self, request, id):
        d = request.POST.dict()
        d['id'] = id
        db_arboles = ArbolesDjango()
        r = db_arboles.update(d)
        return JsonResponse(r)
        
    def delete(self, id):
        db_arboles = ArbolesDjango()
        r = db_arboles.delete({'id': id})
        return JsonResponse(r)


# --- CAMINOS ---
class CaminosView(BaseDjangoView):
    # GET OPERATIONS
    def selectone(self, id):
        db_caminos = CaminosDjango()
        r = db_caminos.selectAsDicts({'id': id}) 
        return JsonResponse(r)

    def selectall(self):
        db_caminos = CaminosDjango()
        # r = db_caminos.selectAll() # Descomenta cuando agregues este método a tu script
        return JsonResponse({"ok": False, "message": "Método selectall no implementado para Caminos aún"})

    # POST OPERATIONS
    def insert(self, request):
        d = request.POST.dict()
        db_caminos = CaminosDjango()
        r = db_caminos.insert(d)
        return JsonResponse(r)
        
    def update(self, request, id):
        d = request.POST.dict()
        d['id'] = id
        db_caminos = CaminosDjango()
        r = db_caminos.update(d)
        return JsonResponse(r)
        
    def delete(self, id):
        db_caminos = CaminosDjango()
        r = db_caminos.delete({'id': id})
        return JsonResponse(r)


# --- PARCELAS ---
class ParcelasView(BaseDjangoView):
    # GET OPERATIONS
    def selectone(self, id):
        db_parcelas = ParcelasDjango()
        r = db_parcelas.selectAsDicts({'id': id}) 
        return JsonResponse(r)

    def selectall(self):
        db_parcelas = ParcelasDjango()
        # r = db_parcelas.selectAll() # Descomenta cuando agregues este método a tu script
        return JsonResponse({"ok": False, "message": "Método selectall no implementado para Parcelas aún"})

    # POST OPERATIONS
    def insert(self, request):
        d = request.POST.dict()
        db_parcelas = ParcelasDjango()
        r = db_parcelas.insert(d)
        return JsonResponse(r)
        
    def update(self, request, id):
        d = request.POST.dict()
        d['id'] = id
        db_parcelas = ParcelasDjango()
        r = db_parcelas.update(d)
        return JsonResponse(r)
        
    def delete(self, id):
        db_parcelas = ParcelasDjango()
        r = db_parcelas.delete({'id': id})
        return JsonResponse(r)
    